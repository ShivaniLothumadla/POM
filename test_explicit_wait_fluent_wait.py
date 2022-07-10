#explicit and fluent waits are very similar,the difference here is we use drv and time out for explicit wait along with condition
#where as we use 2 more params named poll_frequency and ignored_exceptions for fluent wait
'''FluentWait instance defines the maximum amount of time to wait for a condition, as well as the frequency with which to check the condition.

Users may configure the wait to ignore specific types of exceptions whilst waiting, such as NoSuchElementException when searching for an element on the page.'''
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, \
    ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
import pytest

@pytest.fixture()
def test_arrange_cleanup(self):
    self.drv = webdriver.Chrome(ChromeDriverManager().install())
    self.drv.maximize_window()

    self.drv.get('https://www.yatra.com/')
    yield
    self.drv.close()

def test_act(self):
    ele = self.drv.find_element(By.ID, 'BE_flight_origin_city')
    ele.click()
    ele.send_keys('New Delhi')
    ele.send_keys(Keys.ENTER)
    WebDriverWait(self.drv, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]).until(ec.presence_of_element_located((By.ID, 'BE_flight_arrival_city')))
    ele1 = self.drv.find_element(By.ID, "BE_flight_arrival_city")
    ele1.send_keys('New')
    WebDriverWait(self.drv, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]).until(ec.presence_of_all_elements_located((By.XPATH, '//*[@class="viewport"]//div[1]//li')))
    options =self. drv.find_elements_by_xpath('//*[@class="viewport"]//div[1]//li')
    print(len(options))
    for i in options:
        if 'New Delhi (DEL)' in i.text:
            WebDriverWait(self.drv, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]).until(ec.presence_of_all_elements_located((By.XPATH, '//*[@class="viewport"]//div[1]//li')))
            i.click()
            break

