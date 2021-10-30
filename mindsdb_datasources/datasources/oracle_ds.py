import os

import pandas as pd
import cx_Oracle

from mindsdb_datasources.datasources.data_source import SQLDataSource


class OracleDS(SQLDataSource):
    def __init__(self, query, sid='oracle', host='',
                 port, username='', password=''):
        super().__init__(query)
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password
        self.sid=sid

    def query(self, q):
        dsn_tns=cx_Oracle.makedsn(self.host,self.port,self.sid)
        con = cx_Oracle.connect(
            username=self.username,
            password=self.password,
            dsn_tns
        )

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Oracle - {}'.format(self._query)
