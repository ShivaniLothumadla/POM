# https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp
'''
2 types of methods
1. is that the variable will hidden but present in the dom
2.the variable is completely gone from the dom after clicking on something
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
ele = driver.find_element_by_xpath('//*[@id="myDIV"]').is_displayed()
print(ele)
driver.find_element_by_xpath('//*[@id="main"]/button').click()
ele = driver.find_element_by_xpath('//*[@id="myDIV"]').is_displayed()
print(ele)
driver.get('https://www.yatra.com/hotels')
driver.maximize_window()
driver.find_element_by_xpath('//body/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/i[1]').click()
driver.find_element_by_xpath('//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]').click()
ele = driver.find_element_by_xpath('//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/select[1]').is_displayed()
print(ele)
driver.find_element_by_xpath('//body/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]').click()
ele = driver.find_element_by_xpath('//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/select[1]').is_displayed()
print(ele)


