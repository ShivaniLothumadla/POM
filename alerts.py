from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt')
drv.maximize_window()
drv.switch_to.frame(drv.find_element(By.ID, 'iframeResult'))
#accept
drv.find_element(By.XPATH, '//*[text()="Try it"]').click()
sleep(3)
drv.switch_to.alert.accept()

#dismiss
drv.find_element(By.XPATH, '//*[text()="Try it"]').click()
sleep(4)
drv.switch_to.alert.dismiss()

#send_keys
sleep(4)
drv.find_element(By.XPATH, '//*[text()="Try it"]').click()
sleep(4)
drv.switch_to.alert.send_keys('Shivani')
#text
text = drv.switch_to.alert.text
print(text)
drv.switch_to.alert.accept()
sleep(4)



