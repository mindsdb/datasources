import pandas as pd
import prestodb

from mindsdb_datasources.datasources.data_source import SQLDataSource


class PrestoDS(SQLDataSource):
    def __init__(self, query, database, schema, host='localhost',
                 port=8080, user=None, password=None, protocol='https', catalog=None):
        super().__init__(query)
        self.database = database
        self.schema = schema
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.protocol = protocol
        self.catalog = catalog

    def query(self, q):
        con = prestodb.dbapi.connect(
            catalog=self.catalog,
            schema=self.schema,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            http_scheme=self.protocol
        )

        cur = con.cursor().execute(q)
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        df = pd.DataFrame(results)
        cur.close()
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Presto - {}'.format(self._query)
