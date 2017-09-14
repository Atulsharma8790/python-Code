from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.google.co.in")
driver.find_element_by_name("q").send_keys("python")
print driver.title
driver.quit
