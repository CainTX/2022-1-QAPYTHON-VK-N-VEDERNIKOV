import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver


class Base(object):

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def find(self, locator):
        return self.driver.find_element(*locator)

    def get_url(self):
        return self.driver.current_url

    def acquire_attribute(self, locator, attribute):
        elem = self.find(locator)
        return elem.get_attribute(attribute)

    def go_to_url(self, url):
        site = self.driver.get(url)
        return site

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

    def mouse_over(self, locator):
        elem = self.find(locator)
        webdriver.ActionChains(self.driver).move_to_element(elem).perform()

    def switch_window(self, window):
        self.driver.switch_to.window(window)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wd_wait_visibility(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wd_wait_invisibility(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def wd_wait_clickable(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.element_to_be_clickable(locator))

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_letters
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string
