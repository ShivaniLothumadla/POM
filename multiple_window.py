from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
drv = webdriver.Chrome(ChromeDriverManager().install())
drv.get('https://www.yatra.com/')
drv.maximize_window()
drv.find_element(By.XPATH, '//*[@title="FREE CANCELLATION"]').click()
parent_handle = drv.current_window_handle
all_window_handles = drv.window_handles
for i in all_window_handles:
    if i != parent_handle:
        drv.switch_to.window(i)
        from_date = drv.find_element(By.XPATH, '//*[@name="flight_origin" and @placeholder="From"]')
        from_date.click()
        from_date.send_keys('New Delhi')
        from_date.send_keys(Keys.ENTER)
        sleep(5)
        drv.close()
drv.switch_to.window(parent_handle)
check_box = drv.find_element(By.XPATH, '//*[@id="BE_flight_form_wrapper"]/div[3]/div[1]/div[1]/a/i')
check_box.click()
sleep(5)
print(check_box.is_selected())
drv.close()
