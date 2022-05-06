from models import FirstModel, SecondModel, ThirdModel, FourthModel, FifthModel
from util import *


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def session_builder1(self, amount=None):
        param = result_data1()
        amount = amount or param[0][0]

        result = FirstModel(
            amount=amount
        )
        self.client.session.add(result)
        self.client.session.commit()

        return result

    def session_builder2(self, number, status_code=None, amount=None):
        param = result_data2()
        status_code = status_code or param[number][0]
        amount = amount or param[number][1]

        result = SecondModel(
            status_code=status_code,
            amount=amount
        )
        self.client.session.add(result)
        self.client.session.commit()

        return result

    def session_builder3(self, number, url=None, size=None):
        param = result_data3()
        url = url or param[number][1]
        size = size or param[number][2]

        result = ThirdModel(
            url=url,
            size=size
        )
        self.client.session.add(result)
        self.client.session.commit()

        return result

    def session_builder4(self, number, url=None, status_code=None, size=None, ip=None):
        param = result_data4()
        url = url or param[number][1]
        status_code = status_code or param[number][2]
        size = size or param[number][3]
        ip = ip or param[number][4]

        result = FourthModel(
            url=url,
            status_code=status_code,
            size=size,
            ip=ip
        )
        self.client.session.add(result)
        self.client.session.commit()

        return result

    def session_builder5(self, number, ip=None, amount=None):
        param = result_data5()
        ip = ip or param[number][1]
        amount = amount or param[number][2]

        result = FifthModel(
            ip=ip,
            amount=amount
        )
        self.client.session.add(result)
        self.client.session.commit()

        return result
