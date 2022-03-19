import pytest
import random
import string
import credentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators_test import BasicLocators
from selectors_test import BasicSelectors

@pytest.fixture()
def driver():
    service_chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_chrome)
    driver.get(credentials.url)
    driver.maximize_window()
    # Ключевое слово yeild работает только через фикстуру,
    # используя yeild в классе я получаю ошибки, а вот return работает.
    yield driver
    driver.quit()


class Base(BasicSelectors, BasicLocators):

    def login(self, driver):
        self.wdWaitVisibility(self.responseHead_module_button)
        self.search_click(self.responseHead_module_button)
        self.search_send(self.email_locator, credentials.email)
        self.search_send(self.password_locator, credentials.email_password)
        self.search_click(self.authForm_module_button)
        assert driver.current_url == "https://target.my.com/dashboard"

    def logout(self, driver):
        self.wdWaitVisibility(self.href_profile)
        self.wdWaitVisibility(self.spinner_locator)
        self.search_click(self.right_module_rightButton)
        self.mouse_to_element(self.href_logout)
        assert driver.current_url == "https://target.my.com/"

    def info(self, driver):
        # Рандомим значения для имени и телефона

        fio_random = ''.join(random.choice(string.ascii_letters) for i in range(10))
        phone_random = ''.join(random.choice(string.digits) for i in range(10))

        self.wdWaitVisibility(self.href_profile)
        self.search_click(self.href_profile)
        self.wdWaitVisibility(self.fio_locator)
        self.clear_send(self.fio_locator, fio_random)
        self.clear_send(self.phone_locator, phone_random)
        self.search_click(self.button_text)
        self.wdWaitVisibility(self.notification_locator)

        driver.refresh()
        self.wdWaitClickable(self.right_module_userNameWrap)

        fio_check = driver.find_element(By.XPATH, f"// *[text() = '{fio_random}']").is_displayed()
        assert fio_check == True

    def switch(self, current_driver, href, s_text, url):

        self.wdWaitVisibility(self.center_module_buttonsWrap)
        self.wdWaitInvisibility(self.spinner_large_custom_zindex)

        current_driver.find_element(By.XPATH, f'//a[@href="{href}"]').click()

        WebDriverWait(current_driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, f'//span[contains(text(), "{s_text}")]')))

        assert current_driver.current_url == url
