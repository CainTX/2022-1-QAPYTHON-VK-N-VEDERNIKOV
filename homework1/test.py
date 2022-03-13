from conftest import *


class TestBase(Base):
    @pytest.mark.UI
    def test_login(self):
        current_driver = self.driver()
        self.login(current_driver)
        assert current_driver.current_url == "https://target.my.com/dashboard"

    @pytest.mark.UI
    def test_logout(self):
        current_driver = self.driver()
        self.login(current_driver)
        self.logout(current_driver)
        assert current_driver.current_url == "https://target.my.com/"
        current_driver.quit()

    # Тесты для редактирования информации закинул в conftest

    @pytest.mark.UI
    def test_info(self):
        current_driver = self.driver()
        self.login(current_driver)
        self.info(current_driver)
        current_driver.quit()

    # Параметризация работает правильно, только если тесты будут зависимыми,
    # а вот как переделать правильно - у меня нет идей

    testdata = [
        ("/segments", "Список сегментов", "https://target.my.com/segments/segments_list"),
        ("/tools", "Офлайн-конверсии", "https://target.my.com/tools/feeds"),
        ("/billing", "Автопополнение", "https://target.my.com/billing#deposit")
    ]

    @pytest.mark.UI
    @pytest.mark.parametrize("href, s_text, url", testdata)
    def test_switch(self, href, s_text, url):
        current_driver = self.driver()
        self.login(current_driver)
        self.switch(current_driver, href, s_text, url)
