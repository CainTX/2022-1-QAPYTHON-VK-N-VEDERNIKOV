import pytest
from client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table_banner("Total number of requests")
        mysql_client.create_table_banner("Total number of requests by type")
        mysql_client.create_table_banner("Top 10 most frequent requests")
        mysql_client.create_table_banner("Top 5 largest requests resulted in a client error")
        mysql_client.create_table_banner("Top 5 requests that ended with a server error")

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
