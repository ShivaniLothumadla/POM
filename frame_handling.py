from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
drv = webdriver.Chrome(ChromeDriverManager().install())
drv.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css')
drv.maximize_window()
#to work with frames we have to swith to parent/default frame first then switch to the required child frame
#switching frame by id
drv.switch_to.frame('iframeResult')
# #switching frame by name
# drv.switch_to.frame('iframeResult')
# #switching frame by selector
# drv.switch_to.frame('//*[@id="iframeResult"]')
# #switching frame by index
# drv.switch_to.frame(0)
#now switch to the child frame on which our required element present
drv.switch_to.frame(0)
drv.find_element(By.ID, 'w3loginbtn').click()
