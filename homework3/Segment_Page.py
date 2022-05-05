from client import ApiClient
import utility


class SegmentConf(ApiClient):
    def segment_create(self):
        url = "https://target.my.com/api/v2/remarketing/segments.json"
        payload = utility.Segment.segment_json
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}',
        }
        resp = ApiClient.session.post(url, headers=headers, data=payload)
        segment_id = resp.json()["id"]
        SegmentConf.segment_check(self, segment_id)
        return segment_id

# Проверка на совпадения id созданного сегмента

    def segment_check(self, segment_id):
        url = "https://target.my.com/api/v2/remarketing/segments.json?fields=id,name"
        payload = utility.Segment.segment_json
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}',
        }
        resp = ApiClient.session.get(url, headers=headers, data=payload)
        assert segment_id == resp.json()["items"][resp.json()["count"] - 1]["id"]

    def segment_delete(self, id):
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        ApiClient.session.delete(url, headers=headers)
        SegmentConf.segment_delete_check(self, id)

# Проверка удаленного сегмента

    def segment_delete_check(self, id):
        url = f"https://target.my.com/api/v2/remarketing/segments/{id}.json"
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}'
        }
        confirm = ApiClient.session.get(url, headers=headers)
        assert confirm.text == '{"error": {"code": "not_found", "message": "Resource not found", "resource": "Segment"}}'
