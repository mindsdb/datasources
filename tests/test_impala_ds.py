import unittest
from common import DB_CREDENTIALS, break_dataset

@unittest.skip("Ignore untill we have environment ready")
class TestImpala(unittest.TestCase):
    def setUp(self):
        self.HOST = DB_CREDENTIALS['impala']['host']
        self.PORT = int(DB_CREDENTIALS['impala']['port'])
        self.DATABASE = 'impala'

    def test_impala_ds(self):
        from mindsdb_datasources import ImpalaDS

        LIMIT = 100

        impala_ds = ImpalaDS(
            host=self.HOST,
            port=self.PORT,
            database=self.DATABASE,
            query='SELECT * FROM {}.{} LIMIT {}'.format(
                'test_data',
                self.TABLE,
                LIMIT
            )
        )

        impala_ds.df = break_dataset(impala_ds.df)

        assert len(impala_ds) == LIMIT
