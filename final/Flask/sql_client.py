import pymysql
import copy

host = "127.0.0.1"
user = "test_qa"
password = "qa_test"
db_name = "vkeducation"


class Mysql:

    def mysql_setup(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection

    def get_db_values(self, param):
        connection = self.mysql_setup(Mysql)
        try:
            with connection.cursor() as cursor:
                cursor.execute(param)
                rows = cursor.fetchall()
                value = copy.deepcopy(rows)
                return value
        finally:
            connection.close()
