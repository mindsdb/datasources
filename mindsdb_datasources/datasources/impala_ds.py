import impala.dbapi
from impala.util import as_pandas
import pandas as pd

from mindsdb_datasources.datasources.data_source import SQLDataSource


class ImpalaDS(SQLDataSource):
    def __init__(self, query, host='localhost', port=21050, use_ssl=None,
                 ca_cert=None, auth_mechanism='NOSASL', user=None,
                 password=None, database=None):
        super().__init__(query=query)
        self.host = host
        self.port = int(port)
        self.use_ssl = use_ssl
        self.ca_cert = ca_cert
        self.auth_mechanism = auth_mechanism
        self.user = user
        self.password = password
        self.database = database

    def query(self, q):
        con = impala.dbapi.connect(
            host=self.host,
            port=self.port,
            use_ssl=self.use_ssl,
            ca_cert=self.ca_cert,
            auth_mechanism=self.auth_mechanism,
            user=self.user,
            password=self.password,
            database=self.database
        )
        cur = con.cursor()
        cur.execute(q)

        df = as_pandas(cur)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Impala - {}'.format(self._query)
