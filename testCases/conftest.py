from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Firefox()
    driver.get('https://practicetestautomation.com/practice-test-login/')
    return driver
