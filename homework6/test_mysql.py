import pytest
from client import MysqlClient
from builder import MysqlBuilder
from models import FirstModel, SecondModel, ThirdModel, FourthModel, FifthModel


class MyTest:

    def prepare1(self):
        pass

    def prepare2(self):
        pass

    def prepare3(self):
        pass

    def prepare4(self):
        pass

    def prepare5(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql)

        self.prepare1()
        self.prepare2()
        self.prepare3()
        self.prepare4()
        self.prepare5()

    def get_length(self, model_name, **filters):
        self.mysql.session.commit()
        res = self.mysql.session.query(model_name).filter_by(**filters)
        return res.all()

# Не могу создать тесты для всех записей, ловлю ошибку
# sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1062, "Duplicate entry '225133' for key 'test1.PRIMARY'")
# Пробовал менять self.mysql.session.commit() на session.rollback() или session.expunge(obj)
# Но ничего не помогает, тесты запускаются только для одной базы

class TestMySql(MyTest):

    def prepare1(self):
        self.builder.create_test1()

    def prepare2(self):
        for i in range(4):
            self.builder.create_test2(i)

    def prepare3(self):
        for i in range(10):
            self.builder.create_test3(i)

    def test3(self):
        count = self.get_length(ThirdModel)
        assert len(count) == 10

    def prepare4(self):
        for i in range(5):
            self.builder.create_test4(i)

    def prepare5(self):
        for i in range(5):
            self.builder.create_test5(i)
