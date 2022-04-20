from models import FirstModel, SecondModel, ThirdModel, FourthModel, FifthModel
from util import *


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_test1(self, amount=None):
        param = answer_test1()
        test1_amount = amount or param[0][0]

        test1_result = FirstModel(
            amount=test1_amount
        )
        self.client.session.add(test1_result)
        self.client.session.commit()

        return test1_result

    def create_test2(self, number, status_code=None, amount=None):
        param = answer_test2()
        test2_status_code = status_code or param[number][0]
        test2_amount = amount or param[number][1]

        test2_result = SecondModel(
            status_code=test2_status_code,
            amount=test2_amount
        )
        self.client.session.add(test2_result)
        self.client.session.commit()

        return test2_result

    def create_test3(self, number, position=None, url=None, size=None):
        param = answer_test3()
        test3_position = position or param[number][0]
        test3_url = url or param[number][1]
        test3_size = size or param[number][2]

        test3_result = ThirdModel(
            position=test3_position,
            url=test3_url,
            size=test3_size
        )
        self.client.session.add(test3_result)
        self.client.session.commit()

        return test3_result

    def create_test4(self, number, position=None, url=None, status_code=None, size=None, ip=None):
        param = answer_test4()
        test4_position = position or param[number][0]
        test4_url = url or param[number][1]
        test4_status_code = status_code or param[number][2]
        test4_size = size or param[number][3]
        test4_ip = ip or param[number][4]

        test4_result = FourthModel(
            position=test4_position,
            url=test4_url,
            status_code=test4_status_code,
            size=test4_size,
            ip=test4_ip
        )
        self.client.session.add(test4_result)
        self.client.session.commit()

        return test4_result

    def create_test5(self, number, position=None, ip=None, amount=None):
        param = answer_test5()
        test5_position = position or param[number][0]
        test5_ip = ip or param[number][1]
        test5_amount = amount or param[number][2]

        test5_result = FifthModel(
            position=test5_position,
            ip=test5_ip,
            amount=test5_amount
        )
        self.client.session.add(test5_result)
        self.client.session.commit()

        return test5_result
