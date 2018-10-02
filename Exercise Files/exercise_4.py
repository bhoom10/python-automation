from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Bhoomika/python-automation/Exercise%20Files/html_code_01.html")
content = driver.find_element_by_class_name('content')
print("My class element is:")
print(content)
driver.close()
