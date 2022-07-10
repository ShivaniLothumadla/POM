from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import POLL_FREQUENCY

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://jqueryui.com/droppable/')
drv.switch_to.frame(drv.find_element(By.XPATH, "//body/div[@id='container']/div[@id='content-wrapper']/div[1]/div[1]/iframe[1]"))
actions = ActionChains(drv)
source = drv.find_element(By.ID, 'draggable')
destin = drv.find_element(By.ID, 'droppable')
# actions.drag_and_drop(source, destin).perform()
actions.drag_and_drop_by_offset(source, 100, 100).perform()
drv.quit()
