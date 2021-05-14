from mindsdb_datasources.datasources.data_source import DataSource, SQLDataSource
from mindsdb_datasources.datasources.maria_ds import MariaDS
from mindsdb_datasources.datasources.mysql_ds import MySqlDS
from mindsdb_datasources.datasources.clickhouse_ds import ClickhouseDS
from mindsdb_datasources.datasources.file_ds import FileDS
from mindsdb_datasources.datasources.sqlite3_ds import SQLite3DS

from mindsdb_datasources.__about__ import __package_name__ as name, __version__

# These might not initialized properly since they require optional dependencies, so we wrap them in a try-except
try:
    from mindsdb_datasources.datasources.s3_ds import S3DS
except:
    print("S3 Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    S3DS = None

try:
    from mindsdb_datasources.datasources.postgres_ds import PostgresDS
except ImportError:
    print("Postgres Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    PostgresDS = None

try:
    from mindsdb_datasources.datasources.ms_sql_ds import MSSQLDS
except ImportError:
    print("Microsoft SQL Server Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    MSSQLDS = None

try:
    from mindsdb_datasources.datasources.mongodb_ds import MongoDS
except ImportError:
    print("Mongo Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    MongoDS = None

try:
    from mindsdb_datasources.datasources.aws_athena_ds import AthenaDS
except ImportError:
    print("Athena Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    AthenaDS = None

try:
    from mindsdb_datasources.datasources.snowflake_ds import SnowflakeDS
except ImportError:
    print("SnowflakeDS Datasource is not available by default. If you wish to use it, please install mindsdb_native[snowflake]")
    SnowflakeDS = None

try:
    from mindsdb_datasources.datasources.redshift_ds import RedshiftDS
except ImportError:
    print("Redshift Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    RedshiftDS = None

try:
    from mindsdb_datasources.datasources.gcs_ds import GCSDS
except ImportError:
    print("Google Cloud Storage Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    GCSDS = None

try:
    from mindsdb_datasources.datasources.scylla_ds import ScyllaDS
except ImportError:
    print("ScyllaDB Datasource is not available by default. If you wish to use it, please install mindsdb_native[scylla]")
    ScyllaDS = None

try:
    from mindsdb_datasources.datasources.cassandra_ds import CassandraDS
except ImportError:
    print("Cassandra Datasource is not available by default. If you wish to use it, please install mindsdb_native[cassandra]")
    CassandraDS = None
