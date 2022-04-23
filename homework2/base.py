import pytest
from _pytest.fixtures import FixtureRequest
from base_page import BasePage
from campaign_page import CampaignPage
from segment_page import SegmentPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger, request: FixtureRequest):
        self.driver = driver
        self.logger = logger

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.campaign_page: CampaignPage = (request.getfixturevalue('campaign_page'))
        self.segment_page: SegmentPage = (request.getfixturevalue('segment_page'))
