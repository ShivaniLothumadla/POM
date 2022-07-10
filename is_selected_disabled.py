from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.sugarcrm.com/au/request-demo/')

#checkboxes
driver.find_element(By.ID, "interest_market_c0").click()
var = driver.find_element(By.ID, "interest_market_c0").is_selected()
print(var)
var = driver.find_element(By.ID, "interest_sell_c0").is_selected()
print(var)

#radiobuttons
driver.find_element(By.ID, 'doi0').click()
var = driver.find_element(By.ID, 'doi0').is_selected()
print(var)
sleep(4)
driver.find_element(By.ID, 'doi1').click()
var2 = driver.find_element(By.ID, 'doi1').is_selected()
print(var2)