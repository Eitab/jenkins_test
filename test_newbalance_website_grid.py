import time
import warnings
from threading import Thread
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as firefoxService
import pytest_check as check  # install pytest_check package


@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver.exe"
    ser_firefox = firefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()

    browser_name = 'firefox'
    if browser_name == "firefox":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=firefox_options)

    elif browser_name == "MicrosoftEdge":
        dc = {
            "browserName": "MicrosoftEdge",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "Windows 11"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)
    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) "
                                                                     "AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)
    else:
        raise Exception("driver doesn't exists")
    yield driver
    driver.close()


def test_title(driver):
    driver.get("https://www.google.com/")
    title = driver.title
    assert title == "Google"