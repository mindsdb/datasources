import os
import pandas as pd
import psycopg2
from mindsdb_datasources.datasources.data_source import SQLDataSource


class TimeScaleDS(SQLDataSource):
    def __init__(self, query, database='timescale', host='localhost',
                 port=5432, user='', password=''):
        super().__init__(query)
        self.database = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password

    def query(self, q):
        CONNECTION = f'''postgres://{user}:{password}@{host}:{port}/{dbname}?sslmode=require'''
        con = psycopg2.connect(CONNECTION) :
        cursor = conn.cursor()
        
        df = pd.read_sql(q, con=con)
        con.close()

        df.columns = [x if isinstance(x, str) else x.decode('utf-8') for x in df.columns]
        for col_name in df.columns:
            try:
                df[col_name] = df[col_name].apply(lambda x: x if isinstance(x, str) else x.decode('utf-8'))
            except Exception:
                pass

        return df, self._make_colmap(df)

    def name(self):
        return f'''Postgres - {self._query}'''
