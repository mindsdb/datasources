import pandas as pd
import psycopg

from mindsdb_datasources.datasources.data_source import SQLDataSource
from mindsdb_datasources.utilities.ssl import make_ssl_cert


class PostgresDS(SQLDataSource):
    def __init__(self, query, database='postgres', host='localhost',
                 port=5432, user='postgres', password=''):
        super().__init__(query)
        self.database = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password

    def execute(self, query):
        with psycopg.connect(f'host={self.host} port={self.port} dbname={self.database} user={self.user} password={self.password}', connect_timeout=10) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()

    def query(self, q):
        with psycopg.connect(f'host={self.host} port={self.port} dbname={self.database} user={self.user} password={self.password}', connect_timeout=10) as con:
            df = pd.read_sql(q, con=con)

        df.columns = [x if isinstance(x, str) else x.decode('utf-8') for x in df.columns]
        for col_name in df.columns:
            try:
                df[col_name] = df[col_name].apply(lambda x: x if isinstance(x, str) else x.decode('utf-8'))
            except Exception:
                pass

        return df, self._make_colmap(df)

    def name(self):
        return 'Postgres - {}'.format(self._query)
