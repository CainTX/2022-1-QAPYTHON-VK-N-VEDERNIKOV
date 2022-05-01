import utility
from client import ApiClient


class CampaignConf(ApiClient):

    def campaign_create(self):
        url = "https://target.my.com/api/v2/campaigns.json"
        payload = utility.Campaign.campaign_json
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        test_id = ApiClient.session.post(url, headers=headers, data=payload).json()["id"]
        CampaignConf.campaign_check(self, test_id)
        return test_id

    def campaign_check(self, test_id):
        url = "https://target.my.com/api/v2/banners/delivery.json"
        resp = ApiClient.session.get(url).text
        result = resp.find(f"{test_id}")
        if result == 1:
            assert False

    def campaign_delete(self, test_id):
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        url = f"https://target.my.com/api/v2/campaigns/{test_id}.json"
        ApiClient.session.delete(url, headers=headers)
        CampaignConf.campaign_delete_check(self, test_id)

    def campaign_delete_check(self, test_id):
        url = f"https://target.my.com/api/v2/campaigns/{test_id}.json"
        resp = ApiClient.session.get(url).text
        result = resp.find("The campaign is removed.")
        if result == 1:
            assert False
