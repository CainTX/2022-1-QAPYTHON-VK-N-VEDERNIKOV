from conftest import *


class TestBase(Base):

    @pytest.mark.UI
    def test_login(self, driver):
        self.login(driver)

    @pytest.mark.UI
    def test_logout(self, driver):
        self.login(driver)
        self.logout(driver)

    @pytest.mark.UI
    def test_info(self, driver):
        self.login(driver)
        self.info(driver)

    testdata = [
        ("/segments", "Список сегментов", "https://target.my.com/segments/segments_list"),
        ("/tools", "Офлайн-конверсии", "https://target.my.com/tools/feeds"),
        ("/billing", "Автопополнение", "https://target.my.com/billing#deposit")
    ]

    @pytest.mark.UI
    @pytest.mark.parametrize("href, s_text, url", testdata)
    def test_switch(self, href, s_text, url):

        self.login(self.driver)
        self.switch(self.driver, href, s_text, url)
