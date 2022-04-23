from client import *


class SegmentConf(ApiClient):
    def segment_create(self):
        resp = ApiClient.update_cookies(self)
        url = "https://target.my.com/api/v2/remarketing/segments.json"
        payload = conftest.Segment.segment_json
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}',
        }
        resp_seg = resp.post(url, headers=headers, data=payload)
        segment_id = resp_seg.json()["id"]
        SegmentConf.segment_check(self, segment_id)
        return segment_id

# Проверка на совпадения id созданного сегмента

    def segment_check(self, segment_id):
        resp = ApiClient.update_cookies(self)
        url = "https://target.my.com/api/v2/remarketing/segments.json"
        payload = conftest.Segment.segment_json
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}',
        }
        params = {
            "fields": "id, name"
        }
        resp_check = resp.get(url, headers=headers, data=payload, params=params)
        assert segment_id == resp_check.json()["items"][resp_check.json()["count"] - 1]["id"]

    def segment_delete(self, id):
        resp = ApiClient.update_cookies(self)
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        resp.delete(url, headers=headers)
        SegmentConf.segment_delete_check(self, id)

# Проверка удаленного сегмента

    def segment_delete_check(self, id):
        resp = ApiClient.update_cookies(self)
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        confirm = resp.get(url, headers=headers)
        assert confirm.text == '{"error": {"code": "not_found", "message": "Resource not found", "resource": "Segment"}}'
