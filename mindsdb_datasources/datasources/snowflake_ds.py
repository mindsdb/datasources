from mindsdb_datasources.datasources.data_source import SQLDataSource
import pandas as pd
import pyodbc


class SnowflakeDS(SQLDataSource):
    def __init__(self, query, host, user, password, account, warehouse,
                 database, schema, protocol='https', port=443):
        super().__init__(query)
        self.host = host
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.protocol = protocol
        self.port = int(port)

    def query(self, q):
        print(self.host)
        con = pyodbc.connect(f"Driver={{SnowflakeDSIIDriver}}; Server={self.host}; Database={self.database}; schema={self.schema}; UID={self.user}; PWD={self.password}; warehouse={self.warehouse}; protocol={self.protocol}; port={self.port}; account={self.account}")

        cur = con.cursor().execute(q)
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        df = pd.DataFrame(results)
        cur.close()
        con.close()

        return df, self._make_colmap(df)

    def name(self):
        return 'Snowflake - {}'.format(self._query)
