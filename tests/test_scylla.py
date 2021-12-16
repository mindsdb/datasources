import unittest
from common import DB_CREDENTIALS, break_dataset


class TestScylla(unittest.TestCase):
    def setUp(self):
        self.USER = DB_CREDENTIALS['scylla']['user']
        self.PASSWORD = DB_CREDENTIALS['scylla']['password']
        self.HOST = DB_CREDENTIALS['scylla']['host']
        self.PORT = int(DB_CREDENTIALS['scylla']['port'])
        self.KEYSPACE = 'test_data'
        self.TABLE = 'home_rentals'

    def test_scylla_ds(self):
        from mindsdb_datasources import ScyllaDS

        LIMIT = 100

        scylla_ds = ScyllaDS(
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            database=self.KEYSPACE,
            port=self.PORT,
            query='SELECT * FROM {}.{} LIMIT {}'.format(
                'test_data',
                self.TABLE,
                LIMIT
            )
        )

        scylla_ds.df = break_dataset(scylla_ds.df)

        assert len(scylla_ds) == LIMIT

