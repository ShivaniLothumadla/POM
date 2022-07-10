from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.get('https://training.rcvacademy.com/')
#wrkng with javascript
#here the _self is used to open the url in the same window,if you are not passing the _self, then the url is launched in new window
drv.execute_script('window.open("https://training.rcvacademy.com/", "_self");')
sleep(4)
#to get the web element go to console->type document.
# get then you will get all the methods related to get->
# choose one of them like getElementByTagename->pass the tag name as string
# ->will get the webelements associated with that selected tag name->
# choose one of them which is required with the index.
#and return keyword as it is returning the web element.
#note:; is mandatory for javascript methods.
ele = drv.execute_script("return document.getElementsByTagName('p')[1];")
#to click on the web element use arguments[0].click() as a first param,then pass the element you wanted to click on as a second param.
drv.execute_script('arguments[0].click();', ele)
