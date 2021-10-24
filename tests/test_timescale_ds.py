import unittest
from mindsdb_native import F
from common import DB_CREDENTIALS, break_dataset


class TestTimeScale(unittest.TestCase):
    def setUp(self):
        self.USER = DB_CREDENTIALS['postgres']['user']
        self.PASSWORD = DB_CREDENTIALS['postgres']['password']
        self.HOST = DB_CREDENTIALS['postgres']['host']
        self.PORT = int(DB_CREDENTIALS['postgres']['port'])
        self.DATABASE = 'postgres'
        self.TABLE = 'home_rentals'

    def test_timescale_ds(self):
        from mindsdb_datasources import TimeScaleDS

        LIMIT = 100

        timescale_ds = TimeScaleDS(
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            database=self.DATABASE,
            port=self.PORT,
            query='SELECT * FROM {}.{} LIMIT {}'.format(
                'test_data',
                self.TABLE,
                LIMIT
            )
        )

        timescale_ds.df = break_dataset(timescale_ds.df)

        assert len(timescale_ds) == LIMIT

        F.analyse_dataset(timescale_ds)
