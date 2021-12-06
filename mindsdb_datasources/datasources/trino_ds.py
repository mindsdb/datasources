import pandas as pd
import trino

from mindsdb_datasources.datasources.data_source import SQLDataSource


class TrinoDS(SQLDataSource):
    def __init__(self, query, user, password, host='localhost',
                 port=8080, catalog=None, schema='default'):
        super().__init__(query=query)
        self.user = user
        self.password = password
        self.host = host
        self.port = int(port)
        self.catalog = catalog
        self.schema = schema

    def query(self, q):

        con = trino.dbapi.connect(
            self.host,
            self.port,
            self.user,
            catalog=self.catalog, 
            schema=self.schema 
        )

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Trino - {}'.format(self._query)
