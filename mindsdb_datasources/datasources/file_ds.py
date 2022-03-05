import os
from io import BytesIO, StringIO
import csv
import codecs
import json
import traceback
import shutil
from urllib.parse import urlparse
import tempfile

import pandas as pd
import requests

from mindsdb_datasources.datasources.data_source import DataSource
from mindsdb_datasources.utilities.sql import query_df


def clean_row(row):
    n_row = []
    for cell in row:
        if str(cell) in ['', ' ', '  ', 'NaN', 'nan', 'NA']:
            n_row.append(None)
        else:
            n_row.append(cell)

    return n_row


accepted_csv_delimiters = [',', '\t', ';']


class FileDS(DataSource):
    def __init__(self, file, clean_rows=True, custom_parser=None, query=None):
        """
        Setup from file
        :param file: fielpath or url
        :param clean_rows: if you want to clean rows for strange null values
        :param custom_parser: if you want to parse the file with some custom parser
        :param query: filter for file
        """
        if not isinstance(file, str):
            raise ValueError("'file' must be string")
        super().__init__(query=query)
        self.file = file
        self.clean_rows = clean_rows
        self.custom_parser = custom_parser
        self.dialect = None

        self._column_names = None
        self._row_count = None

        self._temp_dir = None

        try:
            self.is_url = urlparse(file).scheme in ('http', 'https')
        except Exception:
            self.is_url = False

    def __del__(self):
        if self._temp_dir is not None:
            shutil.rmtree(self._temp_dir)

    def _handle_source(self):
        self._file_name = os.path.basename(self.file)

        # get file data io, format and dialect
        data, fmt, self.dialect = self._getDataIo(self.file)
        data.seek(0)  # make sure we are at 0 in file pointer

        if self.custom_parser:
            header, file_data = self.custom_parser(data, fmt)

        elif fmt == 'csv':
            csv_reader = list(csv.reader(data, self.dialect))
            header = csv_reader[0]
            file_data = csv_reader[1:]

        elif fmt in ['xlsx', 'xls']:
            data.seek(0)
            df = pd.read_excel(data)
            header = df.columns.values.tolist()
            file_data = df.values.tolist()

        elif fmt == 'json':
            data.seek(0)
            json_doc = json.loads(data.read())
            df = pd.json_normalize(json_doc, max_level=0)
            header = df.columns.values.tolist()
            file_data = df.values.tolist()

        else:
            raise ValueError('Could not load file into any format, supported formats are csv, json, xls, xlsx')

        if self.clean_rows:
            file_list_data = [clean_row(row) for row in file_data]
        else:
            file_list_data = file_data

        col_map = dict((col, col) for col in header)
        return pd.DataFrame(file_list_data, columns=header), col_map

    def query(self, query=None):
        try:
            df, col_map = self._handle_source()
        except Exception as e:
            print(f"Error creating dataframe from handled data: {e}")
            print("pd.read_csv data handler would be used.")
            df = pd.read_csv(self.file, sep=self.dialect.delimiter)
            col_map = dict((col, col) for col in df.columns)
        if query is None:
            return df, col_map

        result_df = query_df(df, query)

        col_map = dict((col, col) for col in result_df.columns)
        return result_df, col_map

    def _getDataIo(self, file):
        """
        This gets a file either url or local file and defiens what the format is as well as dialect
        :param file: file path or url
        :return: data_io, format, dialect
        """

        ############
        # get file as io object
        ############

        file_path = self._get_file_path()

        data = BytesIO()

        try:
            with open(file_path, 'rb') as fp:
                data = BytesIO(fp.read())
        except Exception as e:
            error = 'Could not load file, possible exception : {exception}'.format(exception=e)
            print(error)
            raise ValueError(error)

        dialect = None

        ############
        # check for file type
        ############

        # try to guess if its an excel file
        xlsx_sig = b'\x50\x4B\x05\06'
        # xlsx_sig2 = b'\x50\x4B\x03\x04'
        xls_sig = b'\x09\x08\x10\x00\x00\x06\x05\x00'

        # different whence, offset, size for different types
        excel_meta = [('xls', 0, 512, 8), ('xlsx', 2, -22, 4)]

        for filename, whence, offset, size in excel_meta:

            try:
                data.seek(offset, whence)  # Seek to the offset.
                bytes = data.read(size)  # Capture the specified number of bytes.
                data.seek(0)
                codecs.getencoder('hex')(bytes)

                if bytes == xls_sig:
                    return data, 'xls', dialect
                elif bytes == xlsx_sig:
                    return data, 'xlsx', dialect

            except Exception:
                data.seek(0)

        # if not excel it can be a json file or a CSV, convert from binary to stringio

        byte_str = data.read()
        # Move it to StringIO
        try:
            # Handle Microsoft's BOM "special" UTF-8 encoding
            if byte_str.startswith(codecs.BOM_UTF8):
                data = StringIO(byte_str.decode('utf-8-sig'))
            else:
                data = StringIO(byte_str.decode('utf-8'))

        except Exception:
            print(traceback.format_exc())
            print('Could not load into string')

        # see if its JSON
        buffer = data.read(100)
        data.seek(0)
        text = buffer.strip()
        # analyze first n characters
        if len(text) > 0:
            text = text.strip()
            # it it looks like a json, then try to parse it
            if text.startswith('{') or text.startswith('['):
                try:
                    json.loads(data.read())
                    data.seek(0)
                    return data, 'json', dialect
                except Exception:
                    data.seek(0)
                    return data, None, dialect

        # lets try to figure out if its a csv
        try:
            dialect = self._get_csv_dialect()
            if dialect:
                return data, 'csv', dialect
            return data, None, dialect
        except Exception:
            data.seek(0)
            print('Could not detect format for this file')
            print(traceback.format_exc())
            # No file type identified
            return data, None, dialect

    def name(self):
        return 'File, {}'.format(os.path.basename(self.file))

    def _fetch_url(self):
        if self._temp_dir is not None and os.path.isfile(os.path.join(self._temp_dir, 'file')):
            return
        self._temp_dir = tempfile.mkdtemp(prefix='mindsdb_fileds_')
        try:
            r = requests.get(self.file, stream=True)
            if r.status_code == 200:
                with open(os.path.join(self._temp_dir, 'file'), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
            else:
                raise Exception(f'Responce status code is {r.status_code}')
        except Exception as e:
            print(f'Error during getting {self.file}')
            print(e)
            raise

    def _get_csv_dialect(self) -> object:
        file_path = self._get_file_path()
        with open(file_path, 'rt') as f:
            try:
                dialect = csv.Sniffer().sniff(f.read(128 * 1024), delimiters=accepted_csv_delimiters)
            except csv.Error:
                dialect = None
        return dialect

    def _read_meta(self):
        ''' determine 'column_names' and 'row_count' for DS

            TODO: at this moment optimisation exists only for .csv files,
            all other files will be read whole, which is slow
        '''
        dialect = self._get_csv_dialect()
        if dialect is not None:
            file_path = self._get_file_path()
            with open(file_path) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=dialect.delimiter)
                self._column_names = next(csv_reader, None)
                self._row_count = sum(1 for line in csv_reader)
        else:
            df = self.df
            self._column_names = list(df.keys())
            self._row_count = len(df)

    def _get_file_path(self) -> str:
        path = self.file
        if self.is_url:
            self._fetch_url()
            path = os.path.join(self._temp_dir, 'file')
        return path

    def get_columns(self) -> list:
        if self._column_names is None:
            self._read_meta()
        return self._column_names

    def get_row_count(self) -> int:
        if self._row_count is None:
            self._read_meta()
        return int(self._row_count)
