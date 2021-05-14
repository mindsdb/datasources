from mindsdb_datasources.datasources.scylla_ds import ScyllaDS


class CassandraDS(ScyllaDS):
    ''' Cassandra and ScyllaDB very similar.
        Differ only drivers, but connection can be established with both.
    '''
    def name(self):
        return 'CassandraDB - {}'.format(self._query)
