from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://seleniumhq.org")
element_id = driver.find_element_by_id('q')
print(element_id)

element_name = driver.find_element_by_name('q')
print(element_name)

heading_xpath = driver.find_element_by_xpath("//*[@id='mainContent']/h2[1]")
print(heading_xpath)

element_classname = driver.find_element_by_class_name('selenium-sponsors')
print(element_classname)

driver.close()
