from base import *


class TestAuth(BaseCase):
    @pytest.mark.UI
    def test_negative_auth1(self, driver):
        self.base_page.negative_auth1()

    @pytest.mark.UI
    def test_negative_auth2(self, driver):
        self.base_page.negative_auth2(driver)


class TestCampaign(BaseCase):
    @pytest.mark.UI
    def test_create_campaign(self, driver):
        self.base_page.login(driver)
        self.campaign_page.create_campaign()


class TestSegment(BaseCase):
    @pytest.mark.UI
    def test_create_segment(self, driver):
        self.base_page.login(driver)
        self.segment_page.create_segment(with_delete=False)

    @pytest.mark.UI
    def test_delete_segment(self, driver):
        self.base_page.login(driver)
        self.segment_page.create_segment(driver)
        self.segment_page.delete_segment()
