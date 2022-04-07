import requests
import json
import random
import string
import pytest
from datetime import datetime
import credentials


class ApiClient:

    csrftoken = None
    mrcu = None
    mc = None
    ssdc = None
    sdc = None

    def update_cookies(self, dict=False):
        cookies = [{
            "csrftoken": self.csrftoken,
            "mrcu": self.mrcu,
            "mc": self.mc,
            "ssdc": self.ssdc,
            "sdc": self.sdc,
        }]
        if dict is True:
            return cookies

        r = requests.Session()
        for c in cookies:
            r.cookies.update(c)
        return r

    def post_auth(self):
        headers = {
            'Referer': "https://target.my.com/"
        }
        data = {
            'email': credentials.email,
            'password': credentials.email_password,
            'continue': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email"
        }
        resp = requests.post(url='https://auth-ac.my.com/auth', headers=headers, data=data)
        self.ssdc = resp.history[2].cookies.get("ssdc")
        self.mc = resp.history[2].cookies.get("mc")
        self.mrcu = resp.history[0].cookies.get("mrcu")
        self.sdc = resp.history[4].cookies.get("sdc")
        self.update_cookies(self)


    def get_csrf(self):
        r = ApiClient.update_cookies(self)
        resp = r.get(url='https://target.my.com/csrf/')
        self.csrftoken = resp.cookies.get("csrftoken")
        self.update_cookies(self)
