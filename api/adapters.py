class BigQueryAdapter:
    def fetch_data(self):
        import pandas as pd
        return pd.DataFrame({
            "name": ["A", "B"],
            "value": [10, 20]
        })

import requests

class GraphQLAdapter:
    def fetch_data(self):
        return [{"name": "GraphQL_User", "value": 100}]


class PostgresAdapter:
    def fetch_data(self):
        return [{"name": "DB_User", "value": 200}]


def fetch_from_source(source):
    if source == "bigquery":
        return BigQueryAdapter().fetch_data()
    elif source == "graphql":
        return GraphQLAdapter().fetch_data()
    elif source == "postgres":
        return PostgresAdapter().fetch_data()