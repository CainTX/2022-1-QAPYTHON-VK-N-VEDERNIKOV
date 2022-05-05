import pytest
from Campaign_Page import *
from Segment_Page import SegmentConf


class TestAuth(CampaignConf):
    @pytest.mark.API
    def test_auth(self):
        ApiClient.post_auth(ApiClient)


class TestCampaign(CampaignConf):
    @pytest.mark.API
    def test_campaign(self):
        ApiClient.post_auth(ApiClient)
        CampaignConf.campaign_delete(self, CampaignConf.campaign_create(self))


class TestSegment(SegmentConf):
    @pytest.mark.API
    def test_segment_create(self):
        ApiClient.post_auth(ApiClient)
        SegmentConf.segment_create(self)

    @pytest.mark.API
    def test_segment_delete(self):
        ApiClient.post_auth(ApiClient)
        SegmentConf.segment_delete(self, SegmentConf.segment_create(self))
