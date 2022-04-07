from client import *


class SegmentConf(ApiClient):
    def segment(self, w_delete=False):
        resp = ApiClient.update_cookies(self)
        url = "https://target.my.com/api/v2/remarketing/segments.json"
        payload = json.dumps({
            f"name": f"Сегмент {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "pass_condition": 1,
            "relations": [
                {
                    "id": None,
                    "object_type": "remarketing_campaign_list",
                    "params": {
                        "source_id": 178843,
                        "type": "negative",
                        "event_id": 0,
                        "max_count": 0
                    }
                }
            ],
            "logicType": "or"
        })
        headers = {
            'X-CSRFToken': f'{ApiClient.update_cookies(self, dict=True)[0]["csrftoken"]}',
            'Referer': 'https://target.my.com/segments/segments_list/new'
        }
        resp_seg = resp.post(url, headers=headers, data=payload)
        segment_id = resp_seg.json()["id"]

    # Проверка на совпадения id созданного сегмента

        params = {
            "fields": "id, name"
        }
        resp_j = resp.get(url, headers=headers, data=payload, params=params)
        test_j = resp_j.json()["items"][resp_j.json()["count"] - 1]["id"]
        assert segment_id == test_j

    # Возвращение id для его удаление

        if w_delete is True:
            return segment_id


    def segment_delete(self, id):
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        resp = ApiClient.update_cookies(self)
        headers = {
            'X-CSRFToken': f'{ApiClient.update_cookies(self, dict=True)[0]["csrftoken"]}',
            'Referer': 'https://target.my.com/segments/segments_list/new'
        }
        resp.delete(url, headers=headers)

    # Проверка удаленного сегмента

        url2 = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        confirm = resp.get(url2, headers=headers)
        assert confirm.text == '{"error": {"code": "not_found", "message": "Resource not found", "resource": "Segment"}}'

class CampaignConf(ApiClient):

    def campaign(self, w_delete=False):
        resp = ApiClient.update_cookies(self)
        url = "https://target.my.com/api/v2/campaigns.json"
        payload = json.dumps({
            "name": f"Кампания {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "objective": "traffic",
            "autobidding_mode": "second_price_mean",
            "budget_limit_day": "300",
            "budget_limit": "300000",
            "price": "123",
            "package_id": 961,
            "banners": [
                {
                    "urls": {
                        "primary": {
                            "id": 2024300
                        }
                    },
                    "textblocks": {},
                    "content": {
                        "image_240x400": {
                            "id": 8675863
                        }
                    }
                }
            ]
        })
        headers = {
            'X-CSRFToken': f'{ApiClient.update_cookies(self, dict=True)[0]["csrftoken"]}',
            'Content-Type': 'application/json'
        }
        resp_j = resp.post(url, headers=headers, data=payload)
        test_id = resp_j.json()["id"]

    # Проверка создания кампании

        url2 = "https://target.my.com/api/v2/banners/delivery.json"
        test_j = resp.get(url2).text
        result = test_j.find(f"{test_id}")
        if result == 1:
            assert False

    # Удаление кампании

        if w_delete is True:
            url3 = f"https://target.my.com/api/v2/campaigns/{test_id}.json"
            resp.delete(url3, headers=headers)

    # Проверка удаления кампании

            url4 = f"https://target.my.com/api/v2/campaigns/{test_id}.json"
            test_j = resp.get(url4).text
            result = test_j.find("The campaign is removed.")
            if result == 1:
                assert False
