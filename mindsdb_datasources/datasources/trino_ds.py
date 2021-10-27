import pandas as pd
import trino

from mindsdb_datasources.datasources.data_source import SQLDataSource


class TrinoDS(SQLDataSource):
    def __init__(self, query, catalog, schema, user, host='localhost',
                 port=8080, http_scheme='http', auth=None):
        super().__init__(query=query)
        self.catalog = catalog
        self.schema = schema
        self.user = user
        self.host = host
        self.port = int(port)
        self.http_scheme = http_scheme
        self.auth = auth

    def query(self, q):
        con = trino.dbapi.connect(
            self.host,
            self.port,
            self.user,
            self.catalog,
            self.schema,
            self.http_scheme,
            self.auth
        )

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Trino - {}'.format(self._query)
