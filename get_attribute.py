from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://training.openspan.com/login')
driver.maximize_window()
value = driver.find_element_by_xpath('//*[@id="login_button"]').get_attribute('disabled')
print('@@@@@@@@@@@@@222')
print(value)
