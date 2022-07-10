#perform() would be the last in action chains

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.get('https://www.yatra.com')
drv.maximize_window()
more = drv.find_element(By.XPATH, '//*[text()="+ More"]')
xplore = drv.find_element(By.XPATH, '//*[text()="Xplore"]')
sleep(4)
actions = ActionChains(drv)
actions.move_to_element(more).perform()
sleep(3)
xplore.click()


