from datetime import datetime
import conftest
from client import *


class CampaignConf(ApiClient):

    def campaign_create(self):
        resp = ApiClient.update_cookies(self)
        url = "https://target.my.com/api/v2/campaigns.json"
        payload = conftest.Campaign.campaign_json
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        test_id = resp.post(url, headers=headers, data=payload).json()["id"]
        CampaignConf.campaign_check(self, test_id, resp)
        return test_id

    def campaign_check(self, test_id, resp):
        url2 = "https://target.my.com/api/v2/banners/delivery.json"
        test_j = resp.get(url2).text
        result = test_j.find(f"{test_id}")
        if result == 1:
            assert False

    def campaign_delete(self, test_id):
        resp = ApiClient.update_cookies(self)
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        url3 = f"https://target.my.com/api/v2/campaigns/{test_id}.json"
        resp.delete(url3, headers=headers)
        CampaignConf.campaign_delete_check(self, test_id, resp)

    def campaign_delete_check(self, test_id, resp):
        url4 = f"https://target.my.com/api/v2/campaigns/{test_id}.json"
        test_j = resp.get(url4).text
        result = test_j.find("The campaign is removed.")
        if result == 1:
            assert False
