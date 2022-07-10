from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://www.snapdeal.com/products/mobiles?sort=plrty')
wait = WebDriverWait(drv, 20)
wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="sdHeader"]/div[4]/div[2]/div/div[1]/a[1]/img')))
left = drv.find_element(By.XPATH, '//*[contains(@class,"left-handle")]')
right = drv.find_element(By.XPATH, '//*[contains(@class,"right-handle")]')
actions = ActionChains(drv)
#one way
# actions.drag_and_drop_by_offset(left, 100, 0).perform()
# sleep(4)

sleep(4)
#second way
# actions.click_and_hold(left).pause(2).move_by_offset(50, 0).release().perform()
# sleep(5)

#third way
# actions.move_to_element(left).pause(1).click_and_hold(left).move_by_offset(100, 0).perform()
# sleep(4)
actions.move_to_element(right).pause(3).click_and_hold(right).move_by_offset(-200, 0).perform()
sleep(10)
current_handle = drv.current_window_handle
drv.execute_script('window.open("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=fa201305-94e2-4fca-beeb-3b62c36d4fb3");')
all_hadnles = drv.window_handles
for i in all_hadnles:
    if i != current_handle:
        drv.switch_to.window(i)
        left = drv.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[1]/div')
        right = drv.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[3]/div[1]/div[2]/div')
        actions = ActionChains(drv)
        actions.drag_and_drop_by_offset(left, 100, 0).perform()
        sleep(3)
        actions.drag_and_drop_by_offset(right, 0, 0).perform()
        sleep(3)
        actions.click_and_hold(left).pause(2).move_by_offset(20, 0).perform()
        sleep(5)
        actions.click_and_hold(right).move_by_offset(-20, 0).perform()
        sleep(5)
        actions.move_to_element(left).click_and_hold().move_by_offset(60, 0).perform()
        sleep(5)
        actions.move_to_element(right).click_and_hold().move_by_offset(-60, 0).perform()
drv.quit()
