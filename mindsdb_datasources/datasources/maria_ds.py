from mindsdb_datasources.datasources.mysql_ds import MySqlDS


class MariaDS(MySqlDS):
    def name(self):
        return 'MariaDB - {}'.format(self._query)
