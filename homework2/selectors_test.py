import pytest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import os
import allure


class BasicSelectors:

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            driver.get_screenshot_as_file(screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def find(self, locator):
        return self.driver.find_element(*locator)

    def search_click(self, locator):
        self.find(locator).click()

    def wd_search_click(self, locator):
        self.wait(20).until(expected_conditions.element_to_be_clickable(locator))
        self.find(locator).click()

    def search_send(self, locator, cred):
        self.find(locator).send_keys(cred)

    def clear_input(self, locator):
        self.find(locator).clear()

    def clear_send(self, locator, cred):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(cred)

    def mouse_to_element(self, locator):
        elem = self.find(locator)
        webdriver.ActionChains(self.driver).move_to_element(elem).perform()
        webdriver.ActionChains(self.driver).click(elem).perform()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 20
        return WebDriverWait(self.driver, timeout=timeout)

    def wdWaitVisibility(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wdWaitInvisibility(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def wdWaitClickable(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.element_to_be_clickable(locator))