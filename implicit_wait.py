from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://login.salesforce.com/?locale=in')
drv.implicitly_wait(10)
drv.find_element(By.XPATH, "//input[@id='username']").send_keys('shivani')
drv.find_element(By.XPATH, "//input[@id='password']").send_keys('password')
drv.find_element(By.XPATH, "//input[@id='Login']").click()
drv.close()
