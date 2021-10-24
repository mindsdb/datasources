import os
import unittest
from common import DB_CREDENTIALS


class TestSnowflake(unittest.TestCase):
    def test_snowflake_ds(self):
        print('RUNNING!')
        from mindsdb_datasources import DremioDS

        LIMIT = 100
        # Create the datasource
        dreamio_ds = DremioDS(
            query=f'SELECT * FROM foo.bar LIMIT {LIMIT}',
            host=DB_CREDENTIALS['dremio']['host'],
            user=DB_CREDENTIALS['dremio']['port'],
            password=DB_CREDENTIALS['dremio']['user'],
            account=DB_CREDENTIALS['dremio']['password'],
        )

        assert len(dreamio_ds.df) == LIMIT

