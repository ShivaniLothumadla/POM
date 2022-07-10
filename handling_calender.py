from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
# drv.maximize_window()
drv.get('https://www.yatra.com/')
wait = WebDriverWait(drv, 20)
origin = drv.find_element_by_id("BE_flight_origin_date")
origin.click()
wait.until(ec.presence_of_element_located((By.ID, "19/05/2022")))
# 1st way to click on date(simple way)
# date = drv.find_element_by_id("19/05/2022")
# date.click()
# sleep(4)

#2nd way is to click on date(professional way)
dates = drv.find_elements(By.XPATH, '//*[@id="monthWrapper"]//tbody//*[@class!="inActiveTD"]')
for i in dates:
    if i.get_attribute('data-date') == '22/05/2022':
        i.click()
        sleep(4)
        break


