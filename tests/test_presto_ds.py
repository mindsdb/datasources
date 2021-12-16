import os
import unittest
#from common import DB_CREDENTIALS

@unittest.skip("Ignore untill we have environment ready")
class TestPresto(unittest.TestCase):
    def test_presto_ds(self):
        from mindsdb_datasources import PrestoDS

        # Create the datasource
        presto_ds = PrestoDS(
            query='SELECT * FROM HEALTHCARE_COSTS',
            host=DB_CREDENTIALS['presto']['host'],
            user=DB_CREDENTIALS['presto']['user'],
            password=DB_CREDENTIALS['presto']['password'],
            database=DB_CREDENTIALS['presto']['database'],
            schema=DB_CREDENTIALS['presto']['schema'],
            protocol=DB_CREDENTIALS['presto']['protocol'],
            port=DB_CREDENTIALS['presto']['port'],
            catalog=DB_CREDENTIALS['presto']['catalog'],
        )

        assert len(presto_ds.df) == 1338
        assert len(presto_ds.df.columns) == 7
