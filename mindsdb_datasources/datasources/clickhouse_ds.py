import pandas as pd
import requests
from mindsdb_datasources.datasources.data_source import SQLDataSource


class ClickhouseDS(SQLDataSource):

    def __init__(self,
                 query,
                 database='default',
                 host='localhost',
                 user='default',
                 password='',
                 protocol='http',
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
        self.protocol = protocol

    def query(self, q):
        q = '{} FORMAT JSON'.format(q.rstrip(" ;\n"))
        params = {'user': self.user}
        if self.password is not None:
            params['password'] = self.password
        if self.database is not None:
            params['database'] = self.database
    
        response = requests.post(
            f'{self.protocol}://{self.host}:{self.port}',
            data=q,
            params=params
        )

        try:
            data = response.json()['data']
        except Exception:
            raise Exception(f'Got an invalid response from the database: {response.text}')

        df = pd.DataFrame(data)

        return df, self._make_colmap(df)

    def name(self):
        return 'Clickhouse - {}'.format(self._query)
