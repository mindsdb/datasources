from mindsdb_datasources.datasources.data_source import DataSource, SQLDataSource
from mindsdb_datasources.datasources.maria_ds import MariaDS
from mindsdb_datasources.datasources.mysql_ds import MySqlDS
from mindsdb_datasources.datasources.clickhouse_ds import ClickhouseDS
from mindsdb_datasources.datasources.file_ds import FileDS
from mindsdb_datasources.datasources.sqlite3_ds import SQLite3DS


from mindsdb_datasources.__about__ import __package_name__ as name, __version__

# These might not initialized properly since they require optional dependencies, so we wrap them in a try-except
try:
    from mindsdb_datasources.datasources.snowflake_ds import SnowflakeDS
except ImportError:
    print("SnowflakeDS is not available by default. Please install snowflake's ODBC driver and pyodbc to use it!")
    SnowflakeDS = None

try:
    from mindsdb_datasources.datasources.s3_ds import S3DS
except ImportError:
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

try:
    from mindsdb_datasources.datasources.solr_ds import SolrDS
except ImportError:
    print("Solr Datasource is not available by default.",
          " If you wish to use it, please install Solr and JayDeBeApi.",
          " Then export the Solr JDBC driver to CLASSPATH.",
          " Details: https://solr.apache.org/guide/6_6/solr-jdbc-python-jython.html#jaydebeapi")
    SolrDS = None
    
try:    
    from mindsdb_datasources.datasources.presto_ds import PrestoDS
except:
    print("Presto Darasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    PrestoDS = None

try:
    from mindsdb_datasources.datasources.timescale_ds import TimescaleDS
except ImportError:
    print("Timescale Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    TimescaleDS = None

try:
    from mindsdb_datasources.datasources.dremio_ds import DremioDS
except ImportError:
    print("Dremio Datasource is not available by default. If you wish to use it, please install the Dremio ODBC Driver and pyodbc.")
    DremioDS = None

try:
    from mindsdb_datasources.datasources.bigquery_ds import BigQueryDS
except ImportError:      
    print("BigQuery Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    BigQueryDS = None

try:
    from mindsdb_datasources.datasources.impala_ds import ImpalaDS
except ImportError:
    print("Impala Datasource is not available by default. If you wish to use it, please install mindsdb[extra_data_sources]")
    ImpalaDS = None

    from mindsdb_datasources.datasources.hive_ds import HiveDS
except ImportError:
    print("Hive Datasource is not available by default. If you wish to use it, please install mindsdb[extra_data_sources]")
    HiveDS = None

    from mindsdb_datasources.datasources.trino_ds import TrinoDS
except ImportError:
    print("Trino Datasource is not available by default. If you wish to use it, please install mindsdb[extra_data_sources]")
    TrinoDS = None

try:
    from mindsdb_datasources.datasources.influx_ds import InfluxDS
except ImportError:
    print("InfluxDB Datasource is not available by default. If you wish to use it, please install mindsdb_native[extra_data_sources]")
    InfluxDS = None

try:
    from mindsdb_datasources.datasources.phoenix_ds import PhoenixDS
except ImportError:
    print("Phoenix Datasource is not available by default. If you wish to use it, please install mindsdb[extra_datasources]")
    PhoenixDS = None

try:
    from mindsdb_datasources.datasources.quest_ds import QuestDS
except ImportError:
    print("QuestDB Datasource is not available by default. If you wish to use it, please install mindsdb[extra_datasources]")
    QuestDS = None
