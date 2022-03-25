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

# Драйвер запускается несколько раз при параметризации, скрытие yeild\driver.quit() в def driver не решает проблему.
# Проблема архитектурная, но как переделать так, что-бы driver запускался только 1 раз за параметризацию?
# Пробовал обьявлять драйвер в функции, менять scope на class,session в def driver и def setup, но ответа не нашел.
# Буду рад услышать наводку на решение, или рекомендации к рефакторингу.

        self.login(self.driver)
        self.switch(self.driver, href, s_text, url)
