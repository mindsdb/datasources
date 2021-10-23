import pandas as pd
from jaydebeapi import connect
from mindsdb_datasources.datasources.data_source import SQLDataSource

class Solr(SQLDataSource):
    def __init__(self, query, collection, host='localhost', port=9983,
                 driver='org.apache.solr.client.solrj.io.sql.DriverImpl'):
        super().__init__(query=query)
        self.url = 'jdbc:solr://{}:{}?collection={}'.format(host, port, collection)
        self.driver = driver

    def query(self, q):
        with connect(self.driver, self.url) as con:
            df = pd.read_sql(q, con=con)

        return df, self._make_colmap(df)
    
    def name(self):
        return 'Solr - {}'.format(self._query)