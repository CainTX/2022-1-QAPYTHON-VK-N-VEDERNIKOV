import requests
import json
import random
import string
import pytest
import conftest


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
            'email': conftest.BaseCred.email,
            'password': conftest.BaseCred.email_password,
            'continue': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            'failure': "https://account.my.com/login/"
        }
        resp = requests.Session().post(url='https://auth-ac.my.com/auth', headers=headers, data=data)
        self.mrcu = resp.history[0].cookies.get("mrcu")
        self.ssdc = resp.history[2].cookies.get("ssdc")
        self.mc = resp.history[2].cookies.get("mc")
        self.sdc = resp.history[4].cookies.get("sdc")
        assert self.sdc and self.mrcu and self.ssdc and self.mc is not None
        assert resp.status_code == 200

    def get_csrf(self):
        resp = self.update_cookies(self).get(url='https://target.my.com/csrf/')
        self.csrftoken = resp.cookies.get("csrftoken")
        self.update_cookies(self)
