import os
import unittest
#from common import DB_CREDENTIALS

@unittest.skip("Ignore untill we have environment ready")
class TestDremioDS(unittest.TestCase):
    def test_dremio_ds(self):
        from mindsdb_datasources import DremioDS

        LIMIT = 100

        dremio_ds = DremioDS(
            query=f'SELECT * FROM foo.bar LIMIT {LIMIT}',
            host=DB_CREDENTIALS['dremio']['host'],
            user=DB_CREDENTIALS['dremio']['port'],
            password=DB_CREDENTIALS['dremio']['user'],
        )

        assert len(dremio_ds.df) == LIMIT

