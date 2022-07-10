from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()

#right click
drv.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
rght_clk = drv.find_element(By.XPATH, "//span[text()='right click me']")
actions = ActionChains(drv)
actions.context_click(rght_clk).perform()
sleep(4)
drv.find_element(By.XPATH, './/*[text()="Quit"]').click()
print(drv.switch_to.alert.text)
drv.switch_to.alert.accept()
sleep(4)
current_window = drv.current_window_handle
#double click
#open a new window using javascript
# # drv.execute_script('window.open("https://testautomationpractice.blogspot.com/?m=1", "_self");')
drv.execute_script('window.open("https://testautomationpractice.blogspot.com/?m=1");')
sleep(4)
all_handles = drv.window_handles
for hndle in all_handles:
    if hndle != current_window:
        drv.switch_to.window(hndle)
        sleep(4)
        ele = drv.find_element(By.XPATH, '//*[contains(text(),"Copy Text")]')
        actions = ActionChains(drv)
        actions.double_click(ele).perform()
        sleep(5)
drv.quit()

