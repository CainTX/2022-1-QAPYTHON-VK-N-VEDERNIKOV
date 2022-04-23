import pytest
import logging
import shutil
import string
import random
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import credentials
import allure
from base import BasePage, CampaignPage, SegmentPage


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, temp_dir):
    failed_test_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_test_count:
        browser_logs = os.path.join(temp_dir, 'browser.log')
        with open(browser_logs, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
        screenshot_path = os.path.join(temp_dir, 'failed.png')
        driver.get_screenshot_as_file(screenshot_path)
        allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
        with open(browser_logs, 'r') as f:
            allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)


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


@pytest.fixture
def base_page(driver, logger):
    return BasePage(driver=driver, logger=logger)


@pytest.fixture
def campaign_page(driver, logger):
    return CampaignPage(driver=driver, logger=logger)


@pytest.fixture
def segment_page(driver, logger):
    return SegmentPage(driver=driver, logger=logger)
