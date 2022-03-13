import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Base:

    def driver(self):
        service_chrome = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_chrome)
        driver.get('https://target.my.com')
        driver.maximize_window()
        return driver

    def login(self, driver):
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')))

        driver.find_element(By.XPATH, '//div[contains(@class, "responseHead-module-button")]').click()
        driver.find_element(By.NAME, 'email').send_keys('TXMachine@yandex.ru')
        driver.find_element(By.NAME, 'password').send_keys('txmachine')
        driver.find_element(By.XPATH, '//div[contains(@class,"authForm-module-button")]').click()

    def logout(self, driver):
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//a[@href="/profile"]')))
        WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located(
            (By.XPATH, '//div[contains(@class, "spinner")]')))
        WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'spinner_large_custom_zindex')]")))
        WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'spinner-module-large')]")))

        driver.find_element(By.XPATH, '//div[contains(@class, "right-module-rightButton")]').click()

        elem = driver.find_element(By.XPATH, '//a[@href="/logout"]')

        # Испробовал все вейтеры для rightMenu-module-rightMenu *, но ошибки вылетали нестабильно.
        # Проблема в перемещении кнопки при загрузке, но вот как её обойти? проверка на классы при раскрытии не срабатывает
        # Удалось решить проблему ожиданием исчезновения спинеров, но я бы хотел узнать правильный способ)

        webdriver.ActionChains(driver).move_to_element(elem).perform()
        webdriver.ActionChains(driver).click(elem).perform()

    def info(self, driver):

        # Рандомим значения для имени и телефона

        fio_random = ''.join(random.choice(string.ascii_letters) for i in range(10))
        phone_random = ''.join(random.choice(string.digits) for i in range(10))

        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//a[@href="/profile"]')))

        driver.find_element(By.XPATH, '//a[@href="/profile"]').click()

        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//div[@data-name="fio"]//input[@type="text"]')))

        fio = driver.find_element(By.XPATH, '//div[@data-name="fio"]//input[@type="text"]')
        fio.clear()
        fio.send_keys(fio_random)

        phone = driver.find_element(By.XPATH, '//div[@data-name="phone"]//input[@type="text"]')
        phone.clear()
        phone.send_keys(phone_random)

        driver.find_element(By.XPATH, '//div[contains(@class,"button__text")]').click()

        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class, "_notification_success-bg")]')))

        # Закинул проверки сюда, пока не разобрался как их грамотно перенести в test.py

        driver.refresh()

        WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')))

        fio_check = driver.find_element(By.XPATH, f"// *[text() = '{fio_random}']").is_displayed()
        assert fio_check == True

    def switch(self, current_driver, href, s_text, url):
        WebDriverWait(current_driver, 20).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//ul[contains(@class, "center-module-buttonsWrap")]')))
        WebDriverWait(current_driver, 20).until(expected_conditions.invisibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'spinner_large_custom_zindex')]")))

        current_driver.find_element(By.XPATH, f'//a[@href="{href}"]').click()

        WebDriverWait(current_driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, f'//span[contains(text(), "{s_text}")]')))
        assert current_driver.current_url == url
