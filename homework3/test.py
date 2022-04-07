import pytest

from conftest import *

# Авторизация работает, но я не написал для нее теста, т.к. не знаю, что в ней можно проверить

class TestMain(CampaignConf):
    @pytest.mark.API
    def test_campaign(self):
        ApiClient.post_auth(ApiClient)
        ApiClient.get_csrf(ApiClient)
        ApiClient.update_cookies(ApiClient)
        CampaignConf.campaign(CampaignConf, w_delete=True)

# Объединил создание сегмента и удаление в один тест, чтобы не захламлять раздел,
# По отдельности все работает

class TestSegment(SegmentConf):
    @pytest.mark.API
    def test_segment_create_delete(self):
        ApiClient.post_auth(ApiClient)
        ApiClient.get_csrf(ApiClient)
        ApiClient.update_cookies(ApiClient)
        SegmentConf.segment_delete(SegmentConf, SegmentConf.segment(self, w_delete=True))
