from conftest import *


class TestAuth(AuthCase):
    @pytest.mark.UI
    def test_negative_auth1(self, driver):
        self.negative_auth1()

    @pytest.mark.UI
    def test_negative_auth2(self, driver):
        self.negative_auth2(driver)


class TestCampaign(AuthCase, CampaignCase):
    @pytest.mark.UI
    def test_create_campaign(self, driver):
        self.login(driver)
        self.create_campaign()


class TestSegment(AuthCase, SegmentCase):
    @pytest.mark.UI
    def test_create_segment(self, driver):
        self.login(driver)
        self.create_segment(with_delete=False)

    @pytest.mark.UI
    def test_delete_segment(self, driver):
        self.login(driver)
        self.create_segment(driver)
        self.delete_segment()
