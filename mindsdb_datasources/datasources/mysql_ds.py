import pandas as pd
import mysql.connector

from mindsdb_datasources.datasources.data_source import SQLDataSource


class MySqlDS(SQLDataSource):
    def __init__(self, query, database='mysql', host='localhost',
                 port=3306, user='root', password='',
                 ssl=None, ssl_ca=None, ssl_cert=None, ssl_key=None):
        super().__init__(query)
        self.database = database
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.ssl = ssl
        self.ssl_ca = ssl_ca
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key

    def _get_connection_config(self):
        config = {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "database": self.database
        }
        if self.ssl is True:
            config['client_flags'] = [mysql.connector.constants.ClientFlag.SSL]
            if self.ssl_ca is not None:
                config["ssl_ca"] = self.ssl_ca
            if self.ssl_cert is not None:
                config["ssl_cert"] = self.ssl_cert
            if self.ssl_key is not None:
                config["ssl_key"] = self.ssl_key
        return config

    def execute(self, query):
        config = self._get_connection_config()
        with mysql.connector.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()

    def query(self, q):
        config = self._get_connection_config()
        con = mysql.connector.connect(**config)

        df = pd.read_sql(q, con=con)
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'MySQL - {}'.format(self._query)
