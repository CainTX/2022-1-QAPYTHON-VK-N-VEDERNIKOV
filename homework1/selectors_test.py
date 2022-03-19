import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

class BasicSelectors:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def search_click(self, locator):
        self.find(locator).click()

    def search_send(self, locator, cred):
        self.find(locator).send_keys(cred)

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