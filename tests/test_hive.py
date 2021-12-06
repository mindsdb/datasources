import unittest
from common import DB_CREDENTIALS, break_dataset

@unittest.skip("Ignore untill we have environment ready")
class TestHive(unittest.TestCase):
    def setUp(self):
        self.HOST = DB_CREDENTIALS['hive']['host']
        self.PORT = DB_CREDENTIALS['hive']['port']
        self.DATABASE = 'hive'

    def test_hive_ds(self):
        from mindsdb_datasources import HiveDS

        LIMIT = 100

        hive_ds = HiveDS(
            host=self.HOST,
            port=self.PORT,
            database=self.DATABASE,
            query='SELECT * FROM {}.{} LIMIT {}'.format(
                'test_data',
                self.TABLE,
                LIMIT
            )
        )

        hive_ds.df = break_dataset(hive_ds.df)

        assert len(hive_ds) == LIMIT
