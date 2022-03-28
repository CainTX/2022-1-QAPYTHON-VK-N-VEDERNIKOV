from conftest import *


class TestBase(Base):
    @pytest.mark.UI
    def test_negative_auth1(self, driver):
        self.negative_auth1(driver)

    @pytest.mark.UI
    def test_negative_auth2(self, driver):
        self.negative_auth2(driver)

    @pytest.mark.UI
    def test_create_company(self, driver):
        self.login(driver)
        self.create_company(driver)

    @pytest.mark.UI
    def test_create_segment(self, driver):
        self.login(driver)
        self.create_segment(driver, with_delete=False)

    @pytest.mark.UI
    def test_delete_segment(self, driver):
        self.login(driver)
        self.create_segment(driver)
        self.delete_segment(driver)
