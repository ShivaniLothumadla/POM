from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://www.yatra.com/')
ele = drv.find_element_by_id('BE_flight_origin_city')
ele.click()
ele.send_keys('New Delhi')
ele.send_keys(Keys.ENTER)
sleep(5)
ele1 = drv.find_element_by_id("BE_flight_arrival_city")
sleep(5)
ele1.send_keys('New')
sleep(5)
options = drv.find_elements_by_xpath('//*[@class="viewport"]//div[1]//li')
print(len(options))
for i in options:
    if 'New Delhi (DEL)' in i.text:
        i.click()
        sleep(4)
        break

