import os
import shutil
import tempfile

import pandas as pd
import mysql.connector

from mindsdb_datasources.datasources.data_source import SQLDataSource


class MySqlDS(SQLDataSource):
    def __init__(self, query, database='mysql', host='localhost',
                 port=3306, user='root', password='',
                 ssl=None, ssl_ca=None, ssl_cert=None, ssl_key=None,
                 ssl_ca_name='ssl_ca.pem',
                 ssl_cert_name='ssl_cert.pem',
                 ssl_key_name='ssl_key.pem'):
        super().__init__(query)
        self.database = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self._temp_dir = None
        self.ssl = ssl
        self.ssl_ca = self._get_cert_file_path(ssl_ca_name, ssl_ca)
        self.ssl_cert = self._get_cert_file_path(ssl_cert_name, ssl_cert)
        self.ssl_key = self._get_cert_file_path(ssl_key_name, ssl_key)

    def __del__(self):
        if self._temp_dir is not None:
            shutil.rmtree(self._temp_dir)

    def _get_cert_file_path(self, name: str, cert: str) -> str:
        if isinstance(cert, str) and os.path.isfile(cert) is False:
            if self._temp_dir is None:
                self._temp_dir = tempfile.mkdtemp(prefix='mindsdb_mysql_cert_')
            file_path = os.path.join(self._temp_dir, name)
            with open(file_path, 'wt') as f:
                f.write(cert)
            return file_path
        else:
            return cert

    def query(self, q):
        config = {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "database": self.database
        }
        if self.ssl is True:
            config['client_flags'] = [mysql.connector.constants.ClientFlag.SSL]
            if self.ssl_ca is not None:
                config["ssl_ca"] = self.ssl_ca
            if self.ssl_cert is not None:
                config["ssl_cert"] = self.ssl_cert
            if self.ssl_key is not None:
                config["ssl_key"] = self.ssl_key
        con = mysql.connector.connect(**config)

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'MySQL - {}'.format(self._query)
