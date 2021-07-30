import os

import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from mindsdb_datasources.datasources.data_source import SQLDataSource


class ScyllaDS(SQLDataSource):
    ''' ScyllaDB use CQL, which pretty close to SQL, so filtering and other should work in main cases
        database == keyspace
    '''
    def __init__(self, query, database='', host='localhost', port=9042,
                 user='', password='', secure_connect_bundle=None, protocol_version=None):
        super().__init__(query)
        self.keyspace = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.secure_connect_bundle = secure_connect_bundle
        self.protocol_version = protocol_version

    def query(self, q):
        auth_provider = PlainTextAuthProvider(
            username=self.user, password=self.password
        )
        connection_props = {
            'auth_provider': auth_provider
        }

        if self.protocol_version is not None:
            connection_props['protocol_version'] = self.protocol_version

        if self.secure_connect_bundle is not None:
            if os.path.isfile(self.secure_connect_bundle) is False:
                raise Exception("'secure_connect_bundle' must be path to the file")
            connection_props['cloud'] = {
                'secure_connect_bundle': self.secure_connect_bundle
            }
        else:
            connection_props['contact_points'] = [self.host]
            connection_props['port'] = int(self.port)

        cluster = Cluster(**connection_props)
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
