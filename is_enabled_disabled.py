from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://training.openspan.com/login')
driver.maximize_window()
value = driver.find_element_by_xpath('//*[@id="login_button"]').get_attribute('disabled')
print('@@@@@@@@@@@@@222')
print(value)
value1 = driver.find_element_by_xpath('//*[@id="login_button"]').is_enabled()
print(value1)
driver.find_element_by_xpath('//*[@id="user_name"]').send_keys('abcd')
driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys('1234')
alue = driver.find_element_by_xpath('//*[@id="login_button"]').get_attribute('disabled')
print('@@@@@@@@@@@@@222')
print(value)
value1 = driver.find_element_by_xpath('//*[@id="login_button"]').is_enabled()
print(value1)
