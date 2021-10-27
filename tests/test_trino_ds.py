import unittest
import trino
#from common import DB_CREDENTIALS, break_dataset


@unittest.skip("Ignore untill we have environment ready")
class TrinoDS(unittest.TestCase):
    def setUp(self):
        self.HOST = DB_CREDENTIALS['trino']['host']
        self.PORT = DB_CREDENTIALS['trino']['port']
        self.USER = DB_CREDENTIALS['trino']['user']
        self.CATALOG = 'test-catalog'
        self.SCHEMA = 'test-schema'

    def test_trino_ds(self):
        from mindsdb_datasources import TrinoDS

        LIMIT = 100

        trino_ds = TrinoDS(
            host=self.HOST,
            port=self.PORT,
            user=self.USER,
            catalog=self.CATALOG,
            schema=self.SCHEMA,
            query='SELECT * FROM {}.{} LIMIT {}'.format(
                'test.data',
                self.TABLE,
                LIMIT
            )
        )

        trino_ds.df = break_dataset(trino_ds.df)

        assert len(trino_ds) == LIMIT


