import unittest
from common import DB_CREDENTIALS, break_dataset

@unittest.skip("Ignore untill we have environment ready")
class TestQuestDB(unittest.TestCase):
    def setUp(self):
        self.USER = DB_CREDENTIALS['questdb']['user']
        self.PASSWORD = DB_CREDENTIALS['questdb']['password']
        self.HOST = DB_CREDENTIALS['questdb']['host']
        self.PORT = int(DB_CREDENTIALS['questdb']['port'])
        self.DATABASE = 'questdb'
        self.TABLE = 'test_table'

    def test_postgres_ds(self):
        from mindsdb_datasources import QuestDS

        LIMIT = 100

        quest_ds = QuestDS(
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

        quest_ds.df = break_dataset(quest_ds.df)

        assert len(quest_ds) == LIMIT
