from fixtures import BaseCase
import credentials as cred
import locators
import pytest


class TestReg(BaseCase):

    # UI Регистрация
    @pytest.mark.UI
    def test_basic_reg(self, driver):
        self.reg_page.reg_basic()

    # Проверка полей валидации
    @pytest.mark.UI
    def test_reg_validation(self, driver):
        self.reg_page.reg_validation_check()

    # Переход по ссылке логина
    @pytest.mark.UI
    def test_link_to_auth(self, driver):
        self.reg_page.reg_auth_link()

    # Негативная проверка регистрации без ввода данных
    @pytest.mark.UI
    def test_negative_reg_wo_data(self, driver):
        self.reg_page.negative_reg_wo_data()

    # Негативная проверка с регистрацией уже существующего пользователя
    @pytest.mark.UI
    def test_negative_duplicate_user(self, driver):
        self.reg_page.negative_reg_duplicate_user()

    # Негативная проверка регистрации с существующей почты
    @pytest.mark.UI
    def test_negative_duplicate_mail(self, driver):
        self.reg_page.negative_reg_duplicate_mail()

    # Негативная проверка на регистрацию с неправильным паролем в подтверждении
    @pytest.mark.UI
    def test_negative_wrong_password(self, driver):
        self.reg_page.negative_reg_wrong_password()

    # Негативная проверка для проверки валидации почты
    @pytest.mark.UI
    def test_negative_broken_email_validation(self, driver):
        self.reg_page.negative_reg_broken_email()

    # Негативная проверка на необычные символы при регистрации
    @pytest.mark.UI
    def test_negative_unicode(self, driver):
        self.reg_page.negative_reg_emoji()

    # Негативная проверка SQL и XSS инъекции
    @pytest.mark.UI
    def test_negative_injection(self, driver):
        self.reg_page.negative_reg_injections()


class TestAuth(BaseCase):

    # UI Авторизация
    @pytest.mark.UI
    def test_basic_auth(self, driver):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)

    # Переход по ссылке для создания аккаунта
    @pytest.mark.UI
    def test_reg_link(self, driver):
        self.auth_page.auth_registration_link()

    # Проверка работы валидатора длинны текста
    @pytest.mark.UI
    def test_blank_length(self, driver):
        self.auth_page.auth_short_username()

    # Негативная авторизация без ввода данных
    @pytest.mark.UI
    def test_auth_wo_data(self, driver):
        self.auth_page.negative_auth_wo_data()

    # Негативная проверка пропуска авторизации
    @pytest.mark.UI
    def test_auth_skip(self, driver):
        self.auth_page.negative_skip_auth()

    # Негативная проверка с неправильным паролем
    @pytest.mark.UI
    def test_auth_wrong_password(self, driver):
        self.auth_page.negative_auth_wrong_password()

    # Тестирование SQL инъекции для получения пароля
    @pytest.mark.UI
    def test_auth_injection(self, driver):
        self.auth_page.negative_auth_injection()


class TestApi(BaseCase):

    # Авторизация через API
    @pytest.mark.API
    def test_api_auth(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)

    # Добавление пользователя
    @pytest.mark.API
    def test_api_create_user(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.api_create_user('222', '333', '444',
                                        'FedorXXX', 'education777@mail.com', '555')

    # Смена пароля пользователя
    @pytest.mark.API
    def test_api_password_change(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.api_change_password('FedorXXX', '666')

    # Блокировка пользователя
    @pytest.mark.API
    def test_api_ban_user(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.api_ban_user('FedorXXX')

    # Разблокировка пользователя
    @pytest.mark.API
    def test_api_user_unban(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.api_unban_user('FedorXXX')

    # Удаление пользователя
    @pytest.mark.API
    def test_api_delete_user(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.api_delete_user('FedorXXX')

    # Статус приложения
    @pytest.mark.API
    def test_api_status(self):
        self.api_client.api_status()

    # Неверный url для вывода 404
    @pytest.mark.API
    def test_api_404(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.negative_api_url()

    # Неверный метод у запроса
    @pytest.mark.API
    def test_api_wrong_method(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.negative_wrong_method('FedorXXX')

    # Создание пользователя без json
    @pytest.mark.API
    def test_api_user_create_wo_json(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.negative_user_create_wo_json()

    # Создание пользователя с поломанным json без полей
    @pytest.mark.API
    def test_api_broken_json(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.negative_user_create_broken_json()

    # Создание пользователя через API с превышением ограничения по количеству символов
    @pytest.mark.API
    def test_api_create_user_wo_symbol_limit(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.negative_create_user_wo_limit()

    # Получение FindMeError.js
    @pytest.mark.API
    def test_api_find_error_js(self):
        self.api_client.api_auth(cred.main_username, cred.main_password)
        self.api_client.api_get_error_js()


class TestMain(BaseCase):

    main_locators = locators.MainLocators()

    # Логаут на главной странице
    @pytest.mark.UI
    def test_main_logout(self):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_logout()

    # Проверка отображения данных пользователя
    @pytest.mark.UI
    def test_main_user_creds(self):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_user_creds()

    # Тестирование альтернативного разрешения экрана
    @pytest.mark.UI
    def test_main_screen_resolution(self):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_screen_resolution()

    nav_testdata = [
        (main_locators.main_python, main_locators.main_flask, cred.flask),
        (main_locators.main_linux, main_locators.main_cent_os, cred.cent_os),
        (main_locators.main_network, main_locators.main_news, cred.wire_news)
    ]

    # Тестирование панели навигации
    @pytest.mark.UI
    @pytest.mark.parametrize("dropdown, element, url", nav_testdata)
    def test_main_navbar(self, dropdown, element, url):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_nav_check(dropdown, element, url)

    main_testdata = [
        (main_locators.main_what_api, cred.wiki_api),
        (main_locators.main_future, cred.future),
        (main_locators.main_smtp, cred.smtp)
    ]

    # Тестирование основного контента страницы
    @pytest.mark.UI
    @pytest.mark.parametrize("element, url", main_testdata)
    def test_main_container(self, element, url):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_container_center(element, url)

    # Тест отображения текста в подвале
    @pytest.mark.UI
    def test_main_footer(self):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_footer()

    # Тест отображения 404 ошибки
    @pytest.mark.UI
    def test_main_404(self):
        self.auth_page.auth_basic(cred.main_username, cred.main_password)
        self.main_page.main_404()
