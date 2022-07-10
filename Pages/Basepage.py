from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

"""This class is parent for all the pages.
It contains all the generic methods and utilities for all the classes.
"""
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).send_keys(text)

    def do_get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        result = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator))
        return bool(result)