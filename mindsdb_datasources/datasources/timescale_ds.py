from mindsdb_datasources.datasources.data_source import PostgresDS


class TimescaleDS(PostgresDS):
    def __init__(self,query, database, host,
                 port, user, password):
        super.__init__(query, database, host, port, user, password)

    def name(self):
        return 'Timescale - {}'.format(self._query)