"""#relative xpath
//tagname[@attribute='value']
#absolute xpath
/html/body/...upto the required tag
starts-with:
//tagname[starts-with(@attribute,'value')]   -->value may be partial but the value should starts with the same in the dom
contains():
//tagname[contains(@attribute,'value')]  --->value may be the partial and it is presented in anywhere of the value
text():
//tagname[text()='link text'] --->text is not an attribute its a method so we are not using @ symbol and the value is the link text
And:
//tagname[@attribute='value' and @attribute='value']
OR:
//tagname[@attribute='value or @attribute='value']
axes methods:
self:
//tagname[@attribute='value']//self::tagname
parent:
//tagname[@attribute='value']//parent::tagname
child:
//tagname[@attribute='value']//child::tagname
Ancestor:
//tagname[@attribute''value']//ancestor::tagname
Ancestor-or-self:
//tagname[@attribute='value']//ancestor-or-self::tagname
decendant:
//tagname[@attribute='value']//decendant::tagname
descendant-or-self:
//tagname[@attribute='value']//descendant-or-self::tagname
following:
//tagname[@attribute='value']//following::tagname
following-sibling:
//tagname[@attribute='value']//following-sibling::tagname
preceding:
//tagname[@attribute='value']//preceding::tagname
preceding-sibling:
//tagname[@attribute='value']//preceding-sibling::tagname
"""

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://developer.salesforce.com/signup')
drv.switch_to.default_content()
drv.switch_to.frame('doppler-portal-frame')
drv.find_element(By.XPATH, '//*[@name="first_name"]').send_keys('Shivani')
sleep(4)
drv.close()
