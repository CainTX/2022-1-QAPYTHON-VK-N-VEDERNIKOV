from base import Base
import credentials as cred
import locators
from selenium.common.exceptions import TimeoutException
from sql_client import Mysql


class MainPage(Base):

    main_locators = locators.MainLocators()

    # Логаут на главной странице
    def main_logout(self):
        self.logger.info("Logging out...")
        self.search_click(self.main_locators.main_logout)
        assert self.get_url() == f"{cred.base_url}/login", self.logger.error(f"Logout failed")
        self.logger.info("Successful logout")

    # Проверка отображения данных пользователя
    def main_user_creds(self):
        self.logger.info("Checking user credentials")
        self.wd_wait_clickable(self.main_locators.main_logout)
        logged = self.acquire_attribute(self.main_locators.main_logged, "textContent")
        assert logged == f"Logged as {cred.main_username}", self.logger.error(f"Wrong username")
        user = self.acquire_attribute(self.main_locators.main_user, "textContent")
        assert user == f"User:  {cred.main_name} {cred.main_surname} {cred.main_middle_name}", \
            self.logger.error(f"Missing or wrong user data: {user}")
        try:
            sql_id = Mysql.get_db_values(Mysql, f"SELECT id from test_users where username = '{cred.main_username}'")
            if sql_id[0]["id"] is not None:
                site_id = self.acquire_attribute(self.main_locators.main_vk_id, "textContent")
                assert site_id == f"VK ID: {sql_id[0]['id']}"
        except IndexError:
            assert 0, self.logger.error(f"Missing user from db")
        except AssertionError:
            assert 0, self.logger.error(f"SQL ID doesn't match site ID")
        self.logger.info("User checked successfully")

    # Тестирование альтернативного разрешения экрана
    def main_screen_resolution(self):
        self.logger.info("Trying to lower screen resolution to see auto adjusting")
        self.wd_wait_clickable(self.main_locators.main_logout)
        self.driver.set_window_size(730, 760)
        try:
            self.search_click(self.main_locators.main_home)
        except TimeoutException:
            assert 0, self.logger.error("Elements are blocked")
        self.logger.info("Adjusting is working fine")

    # Тестирование панели навигации
    def main_nav_check(self, dropdown, element, url):
        self.logger.info("Testing navigation panel")
        self.wd_wait_clickable(self.main_locators.main_logout)
        self.mouse_over(dropdown)
        self.search_click(element)
        self.switch_window(self.driver.window_handles[1])
        assert self.get_url() == url, self.logger.error(f"Wrong or broken url, got: {self.get_url()}, expected: {url}")
        self.logger.info("Navigation panel is working fine")

    # Тестирование основного контента страницы
    def main_container_center(self, element, url):
        self.logger.info("Testing main page container")
        self.wd_wait_clickable(self.main_locators.main_logout)
        self.search_click(element)
        self.switch_window(self.driver.window_handles[1])
        assert self.get_url() == url, self.logger.error(f"Wrong or broken url: got: {self.get_url()}, expected: {url}")
        self.logger.info("Main page data links are working fine")

    # Тест отображения текста в подвале
    def main_footer(self):
        self.logger.info("Testing footer data")
        try:
            self.wd_wait_visibility(self.main_locators.main_footer)
            self.wd_wait_visibility(self.main_locators.main_powered)
            self.logger.info("Footer text is displayed")
        except TimeoutException:
            assert 0, self.logger.error("Footer text contain errors or not visible")

    # Тест отображения 404 ошибки
    def main_404(self):
        self.logger.info("Testing 404 page")
        self.go_to_url(f"{cred.base_url}/welcome/404")
        try:
            self.wd_wait_visibility(self.main_locators.main_404)
            self.logger.info("404 Page id displayed")
        except TimeoutException:
            assert 0, self.logger.error("No 404 page is displayed")



