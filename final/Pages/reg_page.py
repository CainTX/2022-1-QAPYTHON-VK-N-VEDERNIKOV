from base import Base
from sql_client import Mysql
import credentials as cred
import locators
from selenium.common.exceptions import TimeoutException


class RegPage(Base):

    reg_locators = locators.RegLocators()

    # UI Регистрация
    def reg_basic(self):
        self.logger.info("Attempting registration...")
        self.go_to_url(f"{cred.base_url}/reg")
        email = self.generate_random_string(10)+"@mail.ru"
        middle_name = self.generate_random_string(5)
        username = self.generate_random_string(6)
        password = self.generate_random_string(7)
        self.reg_data_setup(self.generate_random_string(255), self.generate_random_string(1),
                            middle_name, username, email, password, password)

        sql_result = Mysql.get_db_values(Mysql, f"SELECT * from test_users where username = '{username}'")
        for i in range(4):
            sql_param = ["username", "email", "password", "middle_name"]
            reg_param = [username, email, password, middle_name]
            try:
                assert sql_result[0][sql_param[i]] == reg_param[i]
            except AssertionError:
                self.logger.error(f"Missing {sql_param[i]}:{reg_param[i]} in database")
        Mysql.delete_value(Mysql, f"DELETE FROM test_users WHERE email = '{email}'")
        self.logger.info(f"Successful registration, created user: {username}")

    # Проверка полей валидации
    def reg_validation_check(self):
        self.logger.info("Checking the validation display")
        self.go_to_url(f"{cred.base_url}/reg")
        self.wd_wait_clickable(self.reg_locators.reg_submit)
        self.clear_send(self.reg_locators.reg_username, "Ret")
        self.search_click(self.reg_locators.reg_submit)

        msg_username = self.acquire_attribute(self.reg_locators.reg_username, "validationMessage")
        msg_email = self.acquire_attribute(self.reg_locators.reg_email, "validationMessage")
        msg_password = self.acquire_attribute(self.reg_locators.reg_password, "validationMessage")
        msg_term = self.acquire_attribute(self.reg_locators.reg_term, "validationMessage")
        for i in range(4):
            msg = [msg_username, msg_email, msg_password, msg_term]
            valid_msg = ["Минимально допустимое количество символов: 6. Длина текста сейчас: 3.",
                         "Заполните это поле.", "Чтобы продолжить, установите этот флажок.",
                         "Заполните это поле."]
            error_msg = ["Username", "Email", "Password", "Terms"]
            assert msg[i] == valid_msg[i], self.logger.error(f"Missing validationMessage for {error_msg[i]}")
        self.logger.info("Validation working fine")

    # Переход по ссылке логина
    def reg_auth_link(self):
        self.logger.info("Attempting redirect to login page")
        self.go_to_url(f"{cred.base_url}/reg")
        self.search_click(self.reg_locators.reg_login)
        assert self.get_url() == f"{cred.base_url}/login", self.logger.error(f"Redirect failed, current url:"
                                                                             f" {self.get_url()}")
        self.logger.info("Successfully redirected to login page")

    # Негативная проверка регистрации без ввода данных
    def negative_reg_wo_data(self):
        self.logger.info("Test registration without data")
        self.go_to_url(f"{cred.base_url}/reg")
        self.search_click(self.reg_locators.reg_submit)
        assert self.get_url() == f"{cred.base_url}/reg", self.logger.error(f"Redirect happened, current url:"
                                                                           f" {self.get_url()}")
        self.logger.info("Registration successfully denied")

    # Негативная проверка с регистрацией уже существующего пользователя
    def negative_reg_duplicate_user(self):
        self.logger.info("Registration with already existed account")
        self.reg_user_check()
        self.reg_data_setup(cred.main_name, cred.main_surname, cred.main_middle_name, cred.main_username,
                            cred.main_email, cred.main_password, cred.main_password)
        try:
            self.wd_wait_visibility(self.reg_locators.reg_err_exist)
        except TimeoutException:
            assert 0, self.logger.error("No error message is displayed")
        self.logger.info("Registration successfully denied")

    # Негативная проверка регистрации с существующей почты
    def negative_reg_duplicate_mail(self):
        self.logger.info("Registration with already existed email")
        self.reg_user_check()
        password = self.generate_random_string(6)
        self.reg_data_setup(self.generate_random_string(6), self.generate_random_string(6),
                            self.generate_random_string(6), self.generate_random_string(6),
                            cred.main_email, password, password)
        try:
            self.wd_wait_visibility(self.reg_locators.reg_err_exist)
        except TimeoutException:
            self.wd_wait_invisibility(self.reg_locators.reg_err_exist)
            self.logger.info("Registration successfully denied")
        else:
            assert 0, self.logger.error("Server error | Duplicate mail")

    # Негативная проверка на регистрацию с неправильным паролем в подтверждении
    def negative_reg_wrong_password(self):
        self.logger.info("Registration with wrong password")
        self.reg_data_setup(self.generate_random_string(6), self.generate_random_string(6),
                            self.generate_random_string(6), self.generate_random_string(6),
                            self.generate_random_string(10)+"@mail.ru", "111", "222")
        try:
            self.wd_wait_visibility(self.reg_locators.reg_err_password)
            self.logger.info("Registration successfully denied")
        except TimeoutException:
            assert 0, self.logger.error("No error message is displayed")

    # Негативная проверка для валидации почты
    def negative_reg_broken_email(self):
        self.logger.info("Registration with broken email")
        self.reg_data_setup(self.generate_random_string(6), self.generate_random_string(6),
                            self.generate_random_string(6), self.generate_random_string(6),
                            self.generate_random_string(10), "222", "222")
        try:
            self.wd_wait_visibility(self.reg_locators.reg_err_email)
            self.logger.info("Registration successfully denied")
        except TimeoutException:
            assert 0, self.logger.error("No error message is displayed")

    # Негативная проверка на необычные символы при регистрации
    # Unicode не обрабатывается браузером, но они такие символы вызывают 500ю ошибку (🌎 🌊)
    def negative_reg_emoji(self):
        self.logger.info("Registration with emoji in name")
        mail = self.generate_random_string(10)+"@mail.ru"
        self.reg_data_setup(u'\u2764', u'\u2764', u'\u2764', self.generate_random_string(6),
                            mail, "222", "222")
        sql_result = Mysql.get_db_values(Mysql, f"SELECT * from test_users where email = '{mail}'")
        try:
            self.wd_wait_visibility(self.reg_locators.reg_err_server)
            assert 0, self.logger.error("Server error | Unrecognized symbols")
        except TimeoutException:
            if sql_result[0]['email'] == mail:
                Mysql.delete_value(Mysql, f"DELETE FROM test_users WHERE email = '{mail}'")
                self.logger.info("Successful registration with emoji symbols")

    # Попытка SQL и XSS инъекции
    def negative_reg_injections(self):
        self.logger.info("Trying injecting data")
        script_name = '+alert(document.domain)+'
        script_surname = '<script>console.log("XSSTEST")</script>'
        # Из-за этой строчки, первый раз mysql на несколько секунд выдавал Error code: 1064
        password = "SELECT * FROM test_users WHERE username='Retroweaver' and password='' OR '1'='1'"
        self.reg_data_setup(script_name, script_surname, '', self.generate_random_string(6),
                            self.generate_random_string(10)+"@mail.ru", password, password)
        sql_result = Mysql.get_db_values(Mysql, f"SELECT * from test_users where name = '{script_name}'")
        assert sql_result[0]['password'] == password, self.logger.error(f"Injection succeed, wrong url:"
                                                                        f" {self.get_url()}")
        Mysql.delete_value(Mysql, f"DELETE FROM test_users WHERE name = '{script_name}'")
        self.logger.info("Injection failed successfully")

    # Вспомогательный метод для создания пользователя
    def reg_data_setup(self, name, surname, middle_name, username, email, password, confirm):
        self.go_to_url(f"{cred.base_url}/reg")
        self.wd_wait_clickable(self.reg_locators.reg_submit)
        # У поля name софт-лок в 45 символов
        self.clear_send(self.reg_locators.reg_name, name)
        self.clear_send(self.reg_locators.reg_surname, surname)
        self.clear_send(self.reg_locators.reg_middle_name, middle_name)
        self.clear_send(self.reg_locators.reg_username, username)
        # Валидация по наличию @mail.com
        self.clear_send(self.reg_locators.reg_email, email)
        self.clear_send(self.reg_locators.reg_password, password)
        self.clear_send(self.reg_locators.reg_confirm, confirm)
        self.mouse_to_element(self.reg_locators.reg_term)
        self.search_click(self.reg_locators.reg_submit)

    # Вспомогательный метод для проверки существования тестового пользователя, и его создания
    def reg_user_check(self):
        sql_result = Mysql.get_db_values(Mysql, f"SELECT * from test_users where username = '{cred.main_username}'")
        assert sql_result[0] is not None, self.reg_data_setup(cred.main_name, cred.main_surname, cred.main_middle_name,
                                                              cred.main_username, cred.main_email, cred.main_password,
                                                              cred.main_password)
