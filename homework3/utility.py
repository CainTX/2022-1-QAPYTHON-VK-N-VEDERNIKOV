from datetime import datetime
import json
import random
import string
# from conftest import UniqId


class Segment:
    segment_json = json.dumps({
        f"name": f"Сегмент {''.join(random.choice(string.ascii_letters) for i in range(10))} | {datetime.now().strftime('%Y-%m-%d | %H:%M:%S')} ",
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


class Campaign:

    # UniqId.get_id(UniqId)
    # site_id = UniqId.site_id

    campaign_json = json.dumps({
        "name": f"Кампания {''.join(random.choice(string.ascii_letters) for i in range(10))} | {datetime.now().strftime('%Y-%m-%d | %H:%M:%S')}",
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
                        # "id": f"{site_id}"
                        "id": 12886410
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
