from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import os
import pickle
import locators
import credentials


class BasePage(object):

    locators = locators.BasicLocators()

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def find(self, locator):
        return self.driver.find_element(*locator)

    def search_click(self, locator):
        self.wd_wait_clickable(locator)
        self.find(locator).click()

    def clear_input(self, locator):
        self.wd_wait_visibility(locator)
        self.find(locator).clear()

    def clear_send(self, locator, cred, clear=True):
        if clear is True:
            elem = self.find(locator)
            elem.clear()
            elem.send_keys(cred)
        else:
            self.find(locator).send_keys(cred)

    def mouse_to_element(self, locator):
        elem = self.find(locator)
        webdriver.ActionChains(self.driver).move_to_element(elem).perform()
        webdriver.ActionChains(self.driver).click(elem).perform()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 20
        return WebDriverWait(self.driver, timeout=timeout)

    def wd_wait_visibility(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wd_wait_invisibility(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def wd_wait_clickable(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.element_to_be_clickable(locator))

    def negative_auth1(self):
        self.logger.info("Авторизация без ввода пароля")
        self.search_click(self.locators.auth_responseHead_button)
        self.clear_send(self.locators.auth_email_locator, credentials.email)
        self.clear_input(self.locators.auth_password_locator)
        self.mouse_to_element(self.locators.auth_Form_module_button)

        self.logger.info("Проверка на доступность кнопки авторизации")
        self.find(self.locators.module_disabled_m)

    def negative_auth2(self, driver):
        self.logger.info("Авторизация c неверным паролем")
        self.search_click(self.locators.auth_responseHead_button)
        self.clear_send(self.locators.auth_email_locator, credentials.email)
        self.clear_send(self.locators.auth_password_locator, "123")
        self.search_click(self.locators.auth_Form_module_button)

        self.logger.info("Проверка на отображение страницы с ошибкой")
        self.wd_wait_visibility(self.locators.invalid_pass_check)
        if "login/?error_code" in driver.current_url:
            assert True

    def login(self, driver, w_cookie=True):
        if w_cookie is True and os.path.exists(os.getcwd() + f"\\{credentials.email}_cookies"):
            self.logger.info("Авторизация через куки")
            self.wd_wait_visibility(self.locators.auth_responseHead_button)
            for cookie in pickle.load(open(f"{credentials.email}_cookies", "rb")):
                driver.add_cookie(cookie)
            driver.refresh()
            self.logger.info("Успешная авторизация через куки")

        else:
            self.logger.info("Авторизация вручную")
            self.search_click(self.locators.auth_responseHead_button)
            self.clear_send(self.locators.auth_email_locator, credentials.email)
            self.clear_send(self.locators.auth_password_locator, credentials.email_password)
            self.search_click(self.locators.auth_Form_module_button)
            pickle.dump(driver.get_cookies(), open(f"{credentials.email}_cookies", "wb"))
            self.logger.info("Успешная авторизация вручную")
