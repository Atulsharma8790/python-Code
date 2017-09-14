'''
Created on 02-Sep-2017

@author: atulsharma
'''
from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://www.google.co.in")
driver.find_element_by_name("q").send_keys("Hello Python Selenium")
print driver.title
lists=[]
print driver.find_element_by_name("q").get_attribute("value")
for i in (driver.find_elements_by_tag_name("a")):
    lists.append (i)

print lists.__sizeof__()
for i in range(lists.__sizeof__()):
    print ((lists[i-1]).__getattribute__("text"))
    
driver.quit()
