from google.cloud import bigquery
from mindsdb_datasources.datasources.data_source import SQLDataSource


class BigQueryDS(SQLDataSource):
    def __init__(self, query, project=None, credentials=None,
                 location=None, default_query_job_config=None,
                 client_info=None, client_options=None):
        super().__init__(query)
        self.project = project
        self.credentials = credentials
        self.location = location
        self.default_query_job_config = default_query_job_config
        self.client_info = client_info
        self.client_options = client_options

    def query(self, q):
        client = bigquery.Client(
            project=self.project,
            credentials=self.credentials,
            location=self.location,
            default_query_job_config=self.default_query_job_config,
            client_info=self.client_info,
            client_options=self.client_options
        )
        
        df = client.query(q).to_dataframe()
        client.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Google BigQuery - {}'.format(self._query)

