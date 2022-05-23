import json
import requests
import credentials as cred
from sql_client import Mysql
from base import Base


class ApiClient(Base):

    session = requests.Session()

    # Авторизация через API
    def api_auth(self, username, password):
        payload = {
            "username": username,
            "password": password,
            "submit": "Login"
        }
        self.session.post(url=f'{cred.base_url}/login', data=payload)
        if self.session.cookies.get('session') is not None:
            self.logger.info(f"Successful authentication")
        else:
            assert 0, self.logger.error(f"Authentication error")

    # Добавление пользователя
    def api_create_user(self, name, surname, middle_name, username, email, password):
        payload = cred.cred_user(name, surname, middle_name, username, email, password)
        headers = {
            "Content-Type": "application/json"
        }
        resp = self.session.post(url=f'{cred.base_url}/api/user', data=payload, headers=headers)

        if resp.status_code == 201:
            self.logger.info(f"User: {username} was added")
        elif resp.status_code == 500:
            assert 0, self.logger.error(f"Internal Server Error")
        else:
            self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

        sql_result = Mysql.get_db_values(Mysql, f"SELECT username from test_users where username = '{username}'")
        assert sql_result[0]['username'] == username, self.logger.error("User was not added")

    # Удаление пользователя
    def api_delete_user(self, username):
        resp = self.session.delete(url=f'{cred.base_url}/api/user/{username}')
        if resp.status_code == 204:
            self.logger.info(f"User: {username} was deleted")
        else:
            assert 0, self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

        sql_result = Mysql.get_db_values(Mysql, f"SELECT username from test_users where username = '{username}'")
        assert sql_result == (), self.logger.error("User was not deleted")

    # Смена пароля пользователя
    def api_change_password(self, username, password):
        data = json.dumps({
            "password": f"{password}"
        })
        head = {
            "Content-Type": "application/json"
        }
        resp = self.session.put(url=f'{cred.base_url}/api/user/{username}/change-password', data=data, headers=head)
        if resp.status_code == 204:
            self.logger.info("Password successfully changed")
        else:
            self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

        sql_result = Mysql.get_db_values(Mysql, f"SELECT password from test_users where username = '{username}'")
        assert sql_result[0]['password'] == password, self.logger.error("Wrong password")

    # Блокировка пользователя
    def api_ban_user(self, username):
        resp = self.session.post(url=f'{cred.base_url}/api/user/{username}/block')
        if resp.status_code == 200:
            self.logger.info(f"User: {username} was blocked")
            if resp.json()['status'] != 'success':
                self.logger.error("Response status is missing")
        else:
            self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

        sql_result = Mysql.get_db_values(Mysql, f"SELECT access from test_users where username = '{username}'")
        assert sql_result[0]['access'] == 0, self.logger.error("User was not banned")

    # Разблокировка пользователя
    def api_unban_user(self, username):
        resp = self.session.post(url=f'{cred.base_url}/api/user/{username}/accept')
        if resp.status_code == 200:
            self.logger.info(f"User: {username} access granted")
        else:
            assert 0, self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

        sql_result = Mysql.get_db_values(Mysql, f"SELECT access from test_users where username = '{username}'")
        assert sql_result[0]['access'] == 1, self.logger.error("User was not unbanned")

    # Статус приложения
    def api_status(self):
        resp = self.session.get(url=f'{cred.base_url}/status')
        if resp.json()['status'] == "ok":
            self.logger.info(f"Status: App is working fine")
        else:
            assert 0, self.logger.error(f"Status: App is dead")

    # Неверный url для вывода 404
    def negative_api_url(self):
        resp = self.session.post(url=f'{cred.base_url}/api/user/')
        if resp.status_code != 404:
            assert 0, self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

    # Неверный метод у запроса
    def negative_wrong_method(self, username):
        resp = self.session.get(url=f'{cred.base_url}/api/user/{username}/accept')
        if resp.status_code == 500:
            assert 0, self.logger.error(f"Internal Server Error")

    # Создание пользователя без json
    def negative_user_create_wo_json(self):
        resp = self.session.post(url=f'{cred.base_url}/api/user')
        if resp.status_code == 500:
            assert 0, self.logger.error(f"Internal Server Error")

    # Создание пользователя с поломанным json без полей
    def negative_user_create_broken_json(self):
        payload = {}
        headers = {
            "Content-Type": "application/json"
        }
        resp = self.session.post(url=f'{cred.base_url}/api/user', data=payload, headers=headers)
        if resp.status_code != 201:
            assert 0, self.logger.error(f"Wrong status code: {resp.status_code}, {resp.json()['detail']}")

    # Создание пользователя через API с превышением ограничения по количеству символов
    def negative_create_user_wo_limit(self):
        name = self.generate_random_string(256)
        surname = self.generate_random_string(256)
        middle_name = self.generate_random_string(256)
        username = self.generate_random_string(17)
        email = self.generate_random_string(57)+"@mail.ru"
        password = self.generate_random_string(256)
        self.api_create_user(name, surname, middle_name, username, email, password)

    # Получение FindMeError.js
    def api_get_error_js(self):
        resp = self.session.get(url=f'{cred.base_url}/static/scripts/findMeError.js')
        if resp.status_code == 404:
            assert 0, self.logger.error("File not found")
