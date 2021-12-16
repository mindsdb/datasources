import ssl
import os
import tempfile

import pandas as pd
import pg8000
from mindsdb.utilities.wizards import make_ssl_cert

from mindsdb_datasources.datasources.data_source import SQLDataSource


class PostgresDS(SQLDataSource):
    def __init__(self, query, database='postgres', host='localhost',
                 port=5432, user='postgres', password=''):
        super().__init__(query)
        self.database = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password

    def query(self, q):
        additional_args = {}
        if 'cockroachlabs.cloud' in self.host:
            cert_path = tempfile.mkstemp(prefix='mindsdb_cert_', text=True)[1]
            make_ssl_cert(cert_path)

            ssl_context = ssl.SSLContext()
            ssl_context.load_cert_chain(cert_path)
            additional_args['ssl_context'] = ssl_context

        con = pg8000.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            **additional_args
        )

        df = pd.read_sql(q, con=con)
        con.close()

        if 'cockroachlabs.cloud' in self.host:
            os.remove(cert_path)

        df.columns = [x if isinstance(x, str) else x.decode('utf-8') for x in df.columns]
        for col_name in df.columns:
            try:
                df[col_name] = df[col_name].apply(lambda x: x if isinstance(x, str) else x.decode('utf-8'))
            except Exception:
                pass

        return df, self._make_colmap(df)

    def name(self):
        return 'Postgres - {}'.format(self._query)
