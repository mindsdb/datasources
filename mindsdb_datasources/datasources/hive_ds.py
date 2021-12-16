import pandas as pd
from pyhive import hive

from mindsdb_datasources.datasources.data_source import SQLDataSource


class HiveDS(SQLDataSource):
    def __init__(self, query, host='localhost', port=10000,
                 database='default',  username=None, password=None,
                 auth=None, configuration=None, kerberos_service_name=None,
                 check_hostname=None, scheme='http', ssl_cert=None):

        super().__init__(query=query)
        self.host = host
        self.port = int(port)
        self.database = database
        self.username = username
        self.password = password
        self.auth = auth
        self.configuration = configuration
        self.kerberos_service_name = kerberos_service_name
        self.check_hostname = check_hostname
        self.scheme = scheme
        self.ssl_cert = ssl_cert

    def query(self, q):
        con = hive.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            username=self.username,
            password=self.password,
            auth=self.auth,
            configuration=self.configuration,
            kerberos_service_name=self.kerberos_service_name,
            check_hostname=self.check_hostname,
            scheme=self.scheme,
            ssl_cert=self.ssl_cert,
        )

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Hive - {}'.format(self._query)
