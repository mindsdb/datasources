from mindsdb_datasources.datasources.data_source import PostgresDS


class QuestDS(PostgresDS):
    def __init__(self,query, database, host,
                 port, user, password):
        super.__init__(query, database, host, port, user, password)

    def name(self):
        return 'QuestDB - {}'.format(self._query)
