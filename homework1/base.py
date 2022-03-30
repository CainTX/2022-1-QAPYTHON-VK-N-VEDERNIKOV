import pytest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

