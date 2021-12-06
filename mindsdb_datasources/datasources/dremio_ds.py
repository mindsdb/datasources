import pandas as pd
import pyodbc
from mindsdb_datasources.datasources.data_source import SQLDataSource


class DremioDS(SQLDataSource):
    def __init__(self, query, host, user, password, 
                 driver='Dremio ODBC Driver 64-bit', port=31010):
        super().__init__(query)
        self.host = host
        self.port = int(port)
        self.driver = driver
        self.user = user
        self.password = password

    def query(self, q):
        con = pyodbc.connect(
            f'Driver={self.driver};'
            f'HOST={self.host};'
            f'PORT={self.port};'
            f'UID={self.user};'
            f'PWD={self.password};'
            'AuthenticationType=Plain;'
            'ConnectionType=Direct;'
        )

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Dremio - {}'.format(self._query)

