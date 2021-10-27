import os
import unittest
import logging
from common import DB_CREDENTIALS, break_dataset


class TestMSSQL(unittest.TestCase):
    def test_mssql_ds(self):
        from mindsdb_datasources import MSSQLDS

        HOST = DB_CREDENTIALS['mssql']['host']
        USER = DB_CREDENTIALS['mssql']['user']
        PASSWORD = DB_CREDENTIALS['mssql']['password']
        DATABASE = DB_CREDENTIALS['mssql']['database']
        PORT = DB_CREDENTIALS['mssql']['port']

        mssql_ds = MSSQLDS(
            query='SELECT * FROM dbo.insurance LIMIT',
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT
        )

        assert (len(mssql_ds.df) > 200)
