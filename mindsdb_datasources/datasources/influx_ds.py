import pandas as pd
from influxdb import InfluxDBClient

from mindsdb_datasources.datasources.data_source import SQLDataSource


class InfluxDS(SQLDataSource):
    def __init__(self,query,host, port, 
                username, password, ssl, verify_ssl):
        super().__init__(query)
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password
        self.ssl = ssl
        self.verify_ssl = verify_ssl
    
    def query(self,q):
        client = InfluxDBClient(host=self.host, port=self.port, username=self.username, 
                                password=self.password, ssl=self.ssl, verify_ssl=self.verify_ssl)

        result = client.query(q)
        result = result.raw
        df = pd.json_normalize(result)

        df.columns = [x if isinstance(x, str) else x.decode('utf-8') for x in df.columns]
        for col_name in df.columns:
            try:
                df[col_name] = df[col_name].apply(lambda x: x if isinstance(x, str) else x.decode('utf-8'))
            except Exception:
                pass

        return df, self._make_colmap(df)

