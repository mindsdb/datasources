import pandas as pd
from crate import client

from mindsdb_datasources.datasources.data_source import SQLDataSource 


class CrateDS(SQLDataSource):
    """
    This method takes in the params required for the
    CrateDb connection
    params:
    user: str
    password: str
    hostname: list || str
    port: int
    verify_ssl : bool
    ca_cert: str
    schema: doc

    NOTE: This connection supports multiple host connections
    and SSL
    """

    def __init__(self, query, user, password, hostname, port=4201,
                 verify_ssl=False, ca_cert=None, schema="doc",
                 error_trace=True):
        super().__init__(query)
        self.user = user
        self.password = password
        self.hostname = hostname
        self.port = port
        self.verify_ssl = verify_ssl
        self.ca_cert = ca_cert
        self.schema = schema
        self.error_trace = error_trace

    def query(self, q):
        if self.verify_ssl:
            connection = client.connect(self.hostname,
                                        ca_cert=self.ca_cert,
                                        error_trace=self.error_trace,
                                        username=self.user,
                                        password=self.password,
                                        schema=self.schema)
        connection = client.connect(self.hostname,
                                    verify_ssl_cert=self.verify_ssl,
                                    error_trace=self.error_trace,
                                    username=self.user,
                                    password=self.password,
                                    schema=self.schema)
        df = pd.read_sql(q, con=connection)

        return df, self._make_colmap(df)

    def name(self):
        return 'CrateDB - {}'.format(self._query)

