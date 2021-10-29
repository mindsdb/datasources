import pandas as pd
import phoenixdb

from mindsdb_datasources.datasources.data_source import SQLDataSource


class PhoenixDS(SQLDataSource):
    def __init__(self, query, url, auth=None, authentication=None, user=None,
                 password=None, verify=None):
        super().__init__(query=query)
        self.url = url
        self.auth = auth
        self.authentication = authentication
        self.user = user
        self.password = password
        self.verify = verify

    def query(self, q):
        con = phoenixdb.connect(
            url=self.url,
            auth=self.auth,
            authentication=self.authentication,
            user=self.user,
            password=self.password,
            verify=self.verify
        )

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Phoenix - {}'.format(self._query)
