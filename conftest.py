import time

import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    time.sleep(100)
    driver.quit()
