import pytest
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

    def prepare_session1(self):
        self.builder.session_builder1()

    def prepare_session2(self):
        for i in range(4):
            self.builder.session_builder2(i)

    def prepare_session3(self):
        for i in range(10):
            self.builder.session_builder3(i)

    def prepare_session4(self):
        for i in range(5):
            self.builder.session_builder4(i)

    def prepare_session5(self):
        for i in range(5):
            self.builder.session_builder5(i)


class TestMySql(SetupMySql):

    def test_session1(self):
        self.prepare_session1()
        count = self.get_length(FirstModel)
        assert len(count) == 1
        count2 = self.get_amount(FirstModel, 225133)
        assert len(count2) == 1

    def test_session2(self):
        self.prepare_session2()
        count = self.get_length(SecondModel)
        assert len(count) == 4
        count2 = self.get_amount(SecondModel, 122095)
        assert len(count2) == 1

    def test_session3(self):
        self.prepare_session3()
        count = self.get_length(ThirdModel)
        assert len(count) == 10
        count2 = self.get_size(ThirdModel, 103932)
        assert len(count2) == 1

    def test_session4(self):
        self.prepare_session1()
        count = self.get_length(FourthModel)
        assert len(count) == 5
        count2 = self.get_size(FourthModel, 1417)
        assert len(count2) == 4

    def test_session5(self):
        self.prepare_session5()
        count = self.get_length(FifthModel)
        assert len(count) == 5
        count2 = self.get_amount(FifthModel, 606)
        assert len(count2) == 1

