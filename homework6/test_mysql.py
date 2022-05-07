import pytest
from util import *
from client import MysqlClient
from builder import MysqlBuilder
from models import FirstModel, SecondModel, ThirdModel, FourthModel, FifthModel


class MyTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql)

    def get_length(self, model_name, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(model_name).filter_by(**filters)
        return res.all()

    def get_amount(self, model_name, value):
        self.mysql.session.commit()
        res = self.mysql.session.query(model_name).filter(model_name.amount == value)
        return res.all()

    def get_size(self, model_name, value):
        self.mysql.session.commit()
        res = self.mysql.session.query(model_name).filter(model_name.size == value)
        return res.all()


class SetupMySql(MyTest):

    def prepare_total_requests(self):
        self.builder.session_total_requests()

    def prepare_request_type(self):
        for i in range(4):
            self.builder.session_request_type(i)

    def prepare_frequent_requests(self):
        for i in range(10):
            self.builder.session_frequent_requests(i)

    def prepare_client_error(self):
        for i in range(5):
            self.builder.session_client_error(i)

    def prepare_server_error(self):
        for i in range(5):
            self.builder.session_server_error(i)


class TestMySql(SetupMySql):

    def test_total_requests(self):
        self.prepare_total_requests()
        count = self.get_length(FirstModel)
        assert len(count) == len(result_data1())
        count2 = self.get_amount(FirstModel, result_data1()[0][0])
        assert len(count2) == 1

    def test_request_type(self):
        self.prepare_request_type()
        count = self.get_length(SecondModel)
        assert len(count) == len(result_data2())
        count2 = self.get_amount(SecondModel, result_data2()[0][1])
        assert len(count2) == 1

    def test_frequent_requests(self):
        self.prepare_frequent_requests()
        count = self.get_length(ThirdModel)
        assert len(count) == len(result_data3())
        count2 = self.get_size(ThirdModel, result_data3()[0][2])
        assert len(count2) == 1

    def test_client_error(self):
        self.prepare_client_error()
        count = self.get_length(FourthModel)
        assert len(count) == len(result_data4())
        count2 = self.get_size(FourthModel, result_data4()[0][3])
        assert len(count2) == 4

    def test_server_error(self):
        self.prepare_server_error()
        count = self.get_length(FifthModel)
        assert len(count) == len(result_data5())
        count2 = self.get_amount(FifthModel, result_data5()[0][2])
        assert len(count2) == 1
