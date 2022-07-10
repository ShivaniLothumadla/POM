from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
# drv.maximize_window()
drv.get('https://secure.yatra.com/social/common/yatra/signin.htm')
cntne = drv.find_element(By.ID, 'login-continue-btn')
cntne.screenshot('.\\test.png')
cntne.click()
drv.save_screenshot('.\\test1.png')
drv.get_screenshot_as_file('.\\test2.png')
drv.get_screenshot_as_base64()