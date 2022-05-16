import pytest
from client import MysqlClient


def pytest_configure(config):
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()
    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table_banner("total_requests")
        mysql_client.create_table_banner("total_requests_type")
        mysql_client.create_table_banner("top_frequent_requests")
        mysql_client.create_table_banner("top_requests_client_error")
        mysql_client.create_table_banner("top_requests_server_error")

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
