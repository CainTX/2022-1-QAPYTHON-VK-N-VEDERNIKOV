import shutil
from fixtures import *


def pytest_addoption(parser):
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


def pytest_configure(config):
    base_dir = (os.getcwd() + "\\Base_temp")
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)

    config.base_temp_dir = base_dir
