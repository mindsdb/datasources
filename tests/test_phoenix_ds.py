import unittest
from common import DB_CREDENTIALS, break_dataset


@unittest.skip("Skip untill we resolve dependency issue")
class TestPhoenix(unittest.TestCase):
    def setUp(self):
        self.URL = DB_CREDENTIALS['phoenix']['url']
        self.AUTHENTICATION = 'BASIC'
        self.USER = DB_CREDENTIALS['phoenix']['user']
        self.PASSWORD = DB_CREDENTIALS['phoenix']['password']
        self.TABLE = 'phoenix_test_table'

    def test_phoenix_ds(self):
        from mindsdb_datasources import PhoenixDS

        LIMIT = 100

        phoenix_ds = PhoenixDS(
            url=self.URL,
            authentication=self.AUTHENTICATION,
            user=self.USER,
            password=self.PASSWORD,
            query='SELECT * FROM {}.{} LIMIT {}'.format(
                'test_data',
                self.TABLE,
                LIMIT
            )
        )

        phoenix_ds.df = break_dataset(phoenix_ds.df)

        assert len(phoenix_ds) == LIMIT
