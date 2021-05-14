import os

import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from mindsdb_datasources.datasources.data_source import SQLDataSource


class ScyllaDS(SQLDataSource):
    ''' ScyllaDB use CQL, which pretty close to SQL, so filtering and other should work in main cases
        database == keyspace
    '''
    def __init__(self, query, database='', host='localhost',
                 port=9042, user='', password=''):
        super().__init__(query)
        self.keyspace = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password

    def query(self, q):
        auth_provider = PlainTextAuthProvider(
            username=self.user, password=self.password
        )
        cluster = Cluster([self.host], port=self.port, auth_provider=auth_provider)
        session = cluster.connect()

        if isinstance(self.keyspace, str) and len(self.keyspace) > 0:
            session.set_keyspace(self.keyspace)

        resp = session.execute(q).all()

        df = pd.DataFrame(resp)

        df.columns = [x if isinstance(x, str) else x.decode('utf-8') for x in df.columns]
        for col_name in df.columns:
            try:
                df[col_name] = df[col_name].apply(lambda x: x if isinstance(x, str) else x.decode('utf-8'))
            except Exception:
                pass

        return df, self._make_colmap(df)

    def name(self):
        return 'ScyllaDB - {}'.format(self._query)
