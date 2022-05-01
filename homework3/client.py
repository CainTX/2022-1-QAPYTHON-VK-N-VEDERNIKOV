import requests
import json
import random
import string
import pytest
from cred import BaseCred


class ApiClient:

    session = requests.Session()
    csrftoken = None

    def post_auth(self):
        headers = {
            'Referer': "https://target.my.com/"
        }
        data = {
            'email': BaseCred.email,
            'password': BaseCred.email_password,
            'continue': "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            'failure': "https://account.my.com/login/"
        }
        resp = self.session.post(url='https://auth-ac.my.com/auth', headers=headers, data=data)
        assert self.session.cookies.get('mc') is not None
        assert resp.status_code == 200
        self.get_csrf(self)

    def get_csrf(self):
        self.session.get(url='https://target.my.com/csrf/')
        assert self.session.cookies.get('csrftoken') is not None
        csrf = self.session.cookies.get("csrftoken")
        self.csrftoken = csrf
