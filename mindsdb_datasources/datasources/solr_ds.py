import pandas as pd
import jaydebeapi
from mindsdb_datasources.datasources.data_source import SQLDataSource

class SolrDS(SQLDataSource):
    def __init__(self, query, collection, user, password, host='localhost', port=9983):
        super().__init__(query=query)
        self.url = 'jdbc:solr://{}:{}?collection={}'.format(host, port, collection)
        self.user = user
        self.password = password

    def query(self, q):
        con_properties = {'user': self.user, 'password': self.password}
        con = jaydebeapi.connect('org.apache.solr.client.solrj.io.sql.DriverImpl',
                                 self.url, con_properties)

        df = pd.read_sql(q, con=con)

        con.close()

        return df, self._make_colmap(df)
    
    def name(self):
        return 'Solr - {}'.format(self._query)
