<h1 align="center">
	<img width="300" src="https://github.com/mindsdb/mindsdb_native/blob/stable/assets/MindsDBColorPurp@3x.png?raw=true" alt="MindsDB">
	<br>

</h1>
<div align="center">
	<a href="https://github.com/mindsdb/datasources/actions"><img src="https://github.com/mindsdb/datasources/actions/workflows/mindsdb_datasources.yml/badge.svg" alt="MindsDB Datasources Workflow"></a>
  <a href="https://www.python.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/python-3.6%20|%203.7|%203.8-brightgreen.svg" alt="Python supported"></a>
    <a href="https://join.slack.com/t/mindsdbcommunity/shared_invite/zt-o8mrmx3l-5ai~5H66s6wlxFfBMVI6wQ" target="_blank"><img src="https://img.shields.io/badge/slack-@mindsdbcommunity-brightgreen.svg?logo=slack " alt="MindsDB Community"></a>
	
  <h3 align="center">
    <a href="https://www.mindsdb.com?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo">Website</a>
    <span> | </span>
    <a href="https://docs.mindsdb.com?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo">Docs</a>
    <span> | </span>
  </h3>
  
</div>


## Installation

To install the latest version of MindsDB Datasources use pip:

```
pip install mindsdb_datasources
```

## Overview

MindsDBs Datasources goal is to make it very simple to ingest and prepare data that can be feed into MindsDB as DataSource.


## Datasource Integrations

| Connectors |
|-|
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" alt="Connect MongoDB"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white" alt="Connect MySQL"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="Connect PostgreSQL"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white" alt="Connect MariaDB"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/Apache Kafka-808080?style=for-the-badge&logo=apache-kafka&logoColor=white" alt="Connect MongoDB"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/Snowflake-35aedd?style=for-the-badge&logo=snowflake&logoColor=blue" alt="Connect Snowflake"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/Clickhouse-e6e600?style=for-the-badge&logo=clickhouse&logoColor=white" alt="Connect Clickhouse"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apache%20cassandra&logoColor=white" alt="Connect Cassandra"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white" alt="Connect Redis"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/Microsoft%20SQL%20Sever-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white" alt="Connect SQL Server"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/Singlestore-5f07b4?style=for-the-badge&logo=singlestore&logoColor=white" alt="Connect Singlestore"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/ScyllaDB-53CADD?style=for-the-badge&logo=scylladbb&logoColor=white" alt="Connect ScyllaDB"></a> |
| <a href="https://docs.mindsdb.com/"><img src="https://img.shields.io/badge/CockroachDB-426EDF?style=for-the-badge&logo=cockroachdb&logoColor=white" alt="Connect CockroachDB"></a> |

[:question: :wave: Missing integration?](https://github.com/mindsdb/mindsdb/issues/new?assignees=&labels=&template=feature-mindsdb-request.md)

## Support

If you found a bug, please submit an [issue on Github](https://github.com/mindsdb/mindsdb/issues).

To get community support, you can:
* Post at MindsDB [Slack community](https://join.slack.com/t/mindsdbcommunity/shared_invite/zt-o8mrmx3l-5ai~5H66s6wlxFfBMVI6wQ).
* Ask for help at our [Github Discussions](https://github.com/mindsdb/mindsdb/discussions).
* Ask a question at [Stackoverflow](https://stackoverflow.com/questions/tagged/mindsdb) with a MindsDB tag.

If you need commercial support, please [contact](https://mindsdb.com/contact/?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo) the MindsDB team.

## Contributing

Being part of the core team is accessible to anyone who is motivated and wants to be part of that journey!

If you'd like to contribute to the project, refer to the [contributing documentation](https://docs.mindsdb.com/contribute/?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo).

Please note that this project is released with a [Contributor Code of Conduct](https://github.com/mindsdb/mindsdb/blob/stable/CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## Installing additional dependencies

For some datasources may need additional dependencies.

To work with datasource from list:
```
S3, PostgreSQL, MSSQL, MongoDB, Athena, Redshift, Google Cloud Storage, ScyllaDB, Cassandra, Presto, Timescale, Dremio, Impala, Hive, Trino, InfluxDB, Phoenix, QuestDB, CrateDB
```
please, install dependencies via:
```
pip install mindsdb-datasources[extra_data_sources]
```

If You want to work with `ScyllaDB`, please install:
```
pip install mindsdb-datasources[scylla]
```

If You want to work with `Cassandra`, please install:
```
pip install mindsdb-datasources[cassandra]
```

Note: dependencies for `Cassandra` and `ScyllaDB` may conflict with each other. It would be good not to install them at the same time.

To work with `Snowflake`, please install `Snowflake's ODBC driver` and `pyodbc`.

To work with `Dremio`, please install the `Dremio ODBC Driver` and `pyodbc`.

To work with `Solr`, please install Solr and `JayDeBeApi`. Then export the Solr JDBC driver to CLASSPATH. Details: https://solr.apache.org/guide/6_6/solr-jdbc-python-jython.html#jaydebeapi


## Mailing lists

Subscribe to MindsDB Monthly [Community Newsletter](https://mindsdb.com/newsletter/?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo) to get general announcements, release notes, information about MindsDB events, and the latest blog posts.
You may also join our [beta-users](https://mindsdb.com/beta-tester/?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo) group, and get access to new beta features.


## License

MindsDB is licensed under [GNU General Public License v3.0](https://github.com/mindsdb/mindsdb/blob/master/LICENSE)
