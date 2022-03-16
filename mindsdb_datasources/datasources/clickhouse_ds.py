import pandas as pd
import clickhouse_driver

from mindsdb_datasources.datasources.data_source import SQLDataSource


class ClickhouseDS(SQLDataSource):

    def __init__(self,
                 query,
                 database='default',
                 host='localhost',
                 user='default',
                 password='',
                 port=9000):

        if ' format ' in query.lower():
            raise Exception(
                'Please refrain from adding a "FORMAT" statement to the query')

        super().__init__(query)

        self.database = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password

    def query(self, q):
        with clickhouse_driver.connect(host=self.host,
                                       port=self.port,
                                       database=self.database,
                                       user=self.user,
                                       password=self.password) as con:
            df = pd.read_sql(q, con=con)

        return df, self._make_colmap(df)

    def name(self):
        return 'Clickhouse - {}'.format(self._query)
