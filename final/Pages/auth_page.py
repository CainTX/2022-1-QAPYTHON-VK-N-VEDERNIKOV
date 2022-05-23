from base import Base
import credentials as cred
import locators
from Pages.reg_page import RegPage


class AuthPage(Base):

    auth_locators = locators.AuthLocators()

    # UI Авторизация
    def auth_basic(self, username, password):
        self.logger.info("Authorization...")
        RegPage.reg_user_check(RegPage)
        self.auth_data_setup(username, password)
        assert self.get_url() == f"{cred.base_url}/welcome/", self.logger.error(f"Auth failed")
        self.logger.info(f"Successful authorization by: {username}")

    # Переход по ссылке для создания аккаунта
    def auth_registration_link(self):
        self.logger.info("Redirecting to registration")
        self.search_click(self.auth_locators.auth_reg)
        assert self.get_url() == f"{cred.base_url}/reg", self.logger.error(f"Redirect failed")
        self.logger.info("Successful redirecting to registration")

    # Проверка работы валидатора длинны текста
    def auth_short_username(self):
        self.logger.info("ValidationMessage test auth")
        self.wd_wait_clickable(self.auth_locators.auth_submit)
        self.clear_send(self.auth_locators.auth_username, "Ret")
        msg = self.acquire_attribute(self.auth_locators.auth_username, "validationMessage")
        assert msg == "Минимально допустимое количество символов: 6. Длина текста сейчас: 3.", \
            self.logger.error(f"Validation doesn't work")
        self.logger.info("Validation working fine")

    # Негативная авторизация без ввода данных
    def negative_auth_wo_data(self):
        self.logger.info("Test authorization without data")
        self.auth_data_setup('', '')
        msg = self.acquire_attribute(self.auth_locators.auth_username, "validationMessage")
        assert msg == "Заполните это поле.", self.logger.error(f"Auth with no user data")
        self.logger.info("Successfully failed authorization")

    # Негативная проверка пропуска авторизации
    def negative_skip_auth(self):
        self.logger.info("Trying to skip auth, by going to welcome page")
        self.go_to_url(f"{cred.base_url}/welcome/")
        self.wd_wait_visibility(self.auth_locators.auth_skip)
        assert self.get_url() == f"{cred.base_url}/login?next=/welcome/", self.logger.error(f"Auth skipped")
        self.logger.info("Successfully failed to skip auth")

    # Негативная проверка с неправильным паролем
    def negative_auth_wrong_password(self):
        self.logger.info("Trying auth with incorrect password")
        self.auth_data_setup(cred.main_username, "!322~")
        self.wd_wait_visibility(self.auth_locators.auth_invalid)
        assert self.get_url() == f"{cred.base_url}/login", self.logger.error(f"Wrong password worked")
        self.logger.info("Auth failed successfully")

    # Тестирование SQL инъекции для получения пароля
    def negative_auth_injection(self):
        self.logger.info("Trying injecting password")
        self.auth_data_setup(cred.main_username,
                             "SELECT * FROM test_users WHERE username='Retroweaver' and password='' OR '1'='1'")
        self.wd_wait_visibility(self.auth_locators.auth_invalid)
        assert self.get_url() == f"{cred.base_url}/login", self.logger.error(f"Injection worked")
        self.logger.info("Injection failed successfully")

    def auth_data_setup(self, username, password):
        self.wd_wait_clickable(self.auth_locators.auth_submit)
        self.clear_send(self.auth_locators.auth_username, username)
        self.clear_send(self.auth_locators.auth_password, password)
        self.search_click(self.auth_locators.auth_submit)
