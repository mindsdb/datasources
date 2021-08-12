import os
import unittest
from common import DB_CREDENTIALS


class TestSnowflake(unittest.TestCase):
    def test_snowflake_ds(self):
        print('RUNNING!')
        from mindsdb_datasources import SnowflakeDS

        # Create the datasource
        snowflake_ds = SnowflakeDS(
            query='SELECT * FROM HEALTHCARE_COSTS',
            host=DB_CREDENTIALS['snowflake']['host'],
            user=DB_CREDENTIALS['snowflake']['user'],
            password=DB_CREDENTIALS['snowflake']['password'],
            account=DB_CREDENTIALS['snowflake']['account'],
            warehouse=DB_CREDENTIALS['snowflake']['warehouse'],
            database=DB_CREDENTIALS['snowflake']['database'],
            schema=DB_CREDENTIALS['snowflake']['schema'],
            protocol=DB_CREDENTIALS['snowflake']['protocol'],
            port=DB_CREDENTIALS['snowflake']['port'],
        )

        assert len(snowflake_ds.df) == 1338
        assert len(snowflake_ds.df.columns) == 7
