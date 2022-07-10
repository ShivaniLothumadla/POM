from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://testautomationpractice.blogspot.com/')
#switching to the frame
drv.switch_to.frame('frame-one1434677811')
element = drv.find_element_by_xpath('//*[@id="RESULT_RadioButton-9"]')
drv.execute_script('arguments[0].scrollIntoView();', element)
dd = Select(element)
dd.select_by_index(1)
sleep(4)
dd.select_by_value('Radio-1')
sleep(4)
dd.select_by_visible_text('Evening')
sleep(4)
dd.deselect_by_visible_text('Evening')