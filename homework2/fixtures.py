import pytest
import logging
import shutil
import pickle
import string
import random
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import credentials


# c_name = ("campaign_" + ''.join(random.choice(string.ascii_letters) for i in range(10)))
#
# s_name = ("segment_" + ''.join(random.choice(string.ascii_letters) for g in range(10)))
#
# s_name_a = s_name + "_audit"
#
# ss_name = ("segment_" + ''.join(random.choice(string.ascii_letters) for g in range(10)))
#
# ss_name_a = ss_name + "_audit"

@pytest.fixture()
def driver(config, temp_dir):
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '98.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    else:
        service_chrome = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_chrome)
    driver.get(credentials.url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def logger(temp_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(scope='session')
def config(request):
    if request.config.getoption('--selenoid'):
        if request.config.getoption('--vnc'):
            vnc = True
        else:
            vnc = False
        selenoid = 'http://127.0.0.1:4444/wd/hub'
    else:
        selenoid = None
        vnc = False

    return {
        'selenoid': selenoid,
        'vnc': vnc,
    }


@pytest.fixture(scope='function')
def temp_dir(request):
    temp_dir = os.path.join(request.config.base_temp_dir,
                            "test_" + datetime.now().strftime('%Y-%m-%d %H;%M;%S ') +
                            ''.join(random.choice(string.ascii_letters) for i in range(5)))
    os.makedirs(temp_dir)
    return temp_dir


def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


def pytest_configure(config):
    base_dir = (os.getcwd() + "\\Base_temp")
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)

    config.base_temp_dir = base_dir
