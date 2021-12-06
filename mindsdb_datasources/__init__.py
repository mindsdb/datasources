from mindsdb_datasources.datasources.data_source import DataSource, SQLDataSource
from mindsdb_datasources.datasources.maria_ds import MariaDS
from mindsdb_datasources.datasources.mysql_ds import MySqlDS
from mindsdb_datasources.datasources.clickhouse_ds import ClickhouseDS
from mindsdb_datasources.datasources.file_ds import FileDS
from mindsdb_datasources.datasources.sqlite3_ds import SQLite3DS


from mindsdb_datasources.__about__ import __package_name__ as name, __version__

failed_import_ds = []

# These might not initialized properly since they require optional dependencies, so we wrap them in a try-except
try:
    from mindsdb_datasources.datasources.snowflake_ds import SnowflakeDS
except ImportError:
    failed_import_ds.append('Snowflake')
    SnowflakeDS = None

try:
    from mindsdb_datasources.datasources.s3_ds import S3DS
except:
    failed_import_ds.append('S3')
    S3DS = None

try:
    from mindsdb_datasources.datasources.postgres_ds import PostgresDS
except ImportError:
    failed_import_ds.append('PostgreSQL')
    PostgresDS = None

try:
    from mindsdb_datasources.datasources.ms_sql_ds import MSSQLDS
except ImportError:
    failed_import_ds.append('MSSQL')
    MSSQLDS = None

try:
    from mindsdb_datasources.datasources.mongodb_ds import MongoDS
except ImportError:
    failed_import_ds.append('MongoDB')
    MongoDS = None

try:
    from mindsdb_datasources.datasources.aws_athena_ds import AthenaDS
except ImportError:
    failed_import_ds.append('Athena')
    AthenaDS = None

try:
    from mindsdb_datasources.datasources.redshift_ds import RedshiftDS
except ImportError:
    failed_import_ds.append('Redshift')
    RedshiftDS = None

try:
    from mindsdb_datasources.datasources.gcs_ds import GCSDS
except ImportError:
    failed_import_ds.append('Google Cloud Storage')
    GCSDS = None

try:
    from mindsdb_datasources.datasources.scylla_ds import ScyllaDS
except ImportError:
    failed_import_ds.append('ScyllaDB')
    ScyllaDS = None

try:
    from mindsdb_datasources.datasources.cassandra_ds import CassandraDS
except ImportError:
    failed_import_ds.append('Cassandra')
    CassandraDS = None

try:
    from mindsdb_datasources.datasources.solr_ds import SolrDS
except ImportError:
    failed_import_ds.append('Solr')
    SolrDS = None
    
try:    
    from mindsdb_datasources.datasources.presto_ds import PrestoDS
except:
    failed_import_ds.append('Presto')
    PrestoDS = None

try:
    from mindsdb_datasources.datasources.timescale_ds import TimescaleDS
except ImportError:
    failed_import_ds.append('Timescale')
    TimescaleDS = None

try:
    from mindsdb_datasources.datasources.dremio_ds import DremioDS
except ImportError:
    failed_import_ds.append('Dremio')
    DremioDS = None

try:
    from mindsdb_datasources.datasources.bigquery_ds import BigQueryDS
except ImportError:
    failed_import_ds.append('BigQuery')
    BigQueryDS = None

try:
    from mindsdb_datasources.datasources.impala_ds import ImpalaDS
except ImportError:
    failed_import_ds.append('Impala')
    ImpalaDS = None

try:
    from mindsdb_datasources.datasources.hive_ds import HiveDS
except ImportError:
    failed_import_ds.append('Hive')
    HiveDS = None

try:
    from mindsdb_datasources.datasources.trino_ds import TrinoDS
except ImportError:
    failed_import_ds.append('Trino')
    TrinoDS = None

try:
    from mindsdb_datasources.datasources.influx_ds import InfluxDS
except ImportError:
    failed_import_ds.append('InfluxDB')
    InfluxDS = None

try:
    from mindsdb_datasources.datasources.phoenix_ds import PhoenixDS
except ImportError:
    failed_import_ds.append('Phoenix')
    PhoenixDS = None

try:
    from mindsdb_datasources.datasources.quest_ds import QuestDS
except ImportError:
    failed_import_ds.append('QuestDB')
    QuestDS = None

try:
    from mindsdb_datasources.datasources.crate_ds import CrateDS
except ImportError:
    failed_import_ds.append('CrateDB')
    CrateDS = None

if len(failed_import_ds) > 0:
    print('Some datasources are not available by default. How to install them, read here: https://github.com/mindsdb/datasources#installing-additional-dependencies')
