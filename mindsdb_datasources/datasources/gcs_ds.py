import os

from google.cloud import storage
from google.oauth2 import service_account
import json

from mindsdb_datasources.datasources.data_source import DataSource, FileDS
from mindsdb_datasources import F


class GCSDS(DataSource):
    def __init__(self, bucket_name, file_path, project_id, auth_json):
        super().__init__()
        self.bucket_name = bucket_name
        self.file_path = file_path
        self.auth_json = auth_json
        self.project_id = project_id

    def query(self, q=None):
        try:
            auth_info = json.loads(self.auth_json)
            credentials = service_account.Credentials.from_service_account_info(info=auth_info)
        except Exception:
            credentials = service_account.Credentials.from_service_account_file(filename=self.auth_json)

        gc_client = storage.Client(credentials=credentials, project=self.project_id)
        bucket = gc_client.get_bucket(self.bucket_name)
        blob = storage.Blob(self.file_path, bucket)

        self.tmp_file_name = '.tmp_mindsdb_data_file'

        with open(self.tmp_file_name, 'wb') as fw:
            gc_client.download_blob_to_file(blob, fw)

        file_ds = FileDS(self.tmp_file_name)

        os.remove(self.tmp_file_name)

        return file_ds.df, file_ds._col_map

    def name(self):
        return 'GCS - {}/{}'.format(self.bucket_name, os.path.basename(self.file_path))
