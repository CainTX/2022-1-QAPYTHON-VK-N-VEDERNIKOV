from client import ApiClient


class UniqImage(ApiClient):

    def get_image(self):
        url = 'https://target.my.com/api/v2/content/static.json'
        headers = {
            'X-CSRFToken': self.csrftoken,
        }
        file = {
            'file': open("240p.png", 'rb'),
        }
        data = {
            "width": 0,
            "height": 0
        }
        return ApiClient.session.post(url, files=file, headers=headers, data=data).json()['id']

    def get_image_id(self):
        ApiClient.post_auth(ApiClient)
        resp = UniqImage.get_image(UniqImage)
        print(resp)
        return resp


class UniqId(ApiClient):

    def get_url(self):
        url = "https://target.my.com/api/v1/urls/"
        headers = {
            'X-CSRFToken': f'{ApiClient.csrftoken}',
        }
        params = {
            "url": "https://www.google.com/"
        }
        return ApiClient.session.get(url, headers=headers, params=params).json()['id']

    def get_url_id(self):
        ApiClient.post_auth(ApiClient)
        resp = UniqId.get_url(UniqId)
        print(resp)
        return resp
