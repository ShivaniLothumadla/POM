"""
css selector:
css:cascading style sheet
1.id:
tagname[id=value]
tagname#value
2.class:
tagname[class=value]
tagname.value
3.any other attributes:
tagname[attribute='value'] -->value should be in quotes for other attributes.(some cases required.)
img[alt='Top Offers']
4.we can combine the attributes
tagname#id_value[type='value'][value='value']
5.startswith(^), ends($) with and middle(*):
6.child and (child or sub-child):
child:  --using >
tagname[attribute=value] > tagname[attribute=value]
child or sub child: using space
tagname[attribute=value] tagname[attribute=value]
7.next sibling or adjacent sibling using +
tagname[attribute=value]+tagname[attribute=value]
Pseudo classes:
8.first-child, last-child, nth-child(), nth-last-child()
tagname[attribute=value]
9.firt-of-type, last-of-type and nth-of-type based on the tags of children
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

drv = webdriver.Chrome(ChromeDriverManager().install())
drv.maximize_window()
drv.get('https://www.flipkart.com/')

#using id as attribute,we can use # symbol to represt id
drv.find_element(By.CSS_SELECTOR, 'div#container')
drv.find_element(By.CSS_SELECTOR, 'div[id=container]')

#using class as attribute we use . symbol to represent class
drv.find_element(By.CSS_SELECTOR, 'a[class="_1_3w1N"]')
drv.find_element(By.CSS_SELECTOR, 'a._1_3w1N')

#using multiple attributes
drv.find_element(By.CSS_SELECTOR, '*._2xm1JU[alt=Flipkart][title=Flipkart]')

#using ^, $ and *
drv.find_element(By.CSS_SELECTOR, '*[placeholder$="brands and more"]') # matches with the end of the text
drv.find_element(By.CSS_SELECTOR, '*[placeholder^="Search for products"]') #matches with the beginning of the text.Like starts-with() in xpath
drv.find_element(By.CSS_SELECTOR, '*[placeholder*="Search for products, brands and more"]') #matches from anywhere of the text.like contains() in xpath

#using child (>) and sub child ()
drv.find_element(By.CSS_SELECTOR, "*[class*='col-12-12']>input")
drv.find_element(By.CSS_SELECTOR, "*[class*='col-12-12']>input")

#using + for adjacent or next sibling
drv.find_element(By.CSS_SELECTOR, "input[name='marketplace']+*")


# 8.first-child, last-child, nth-child(), nth-last-child()
drv.find_element(By.CSS_SELECTOR, '*[class="_2Xfa2_"]>div:nth-last-child(5)')
#first-of-type, last-of-type and nth-of-type() to findout based on the tags you wanted to.
drv.find_element(By.CSS_SELECTOR, '*[class="_2Xfa2_"]>div:nth-of-type(4)')
drv.find_element(By.CSS_SELECTOR, '*[class="_2Xfa2_"]>div:first-of-type')
drv.find_element(By.CSS_SELECTOR, '*[class="_2Xfa2_"]>div:last-of-type')


