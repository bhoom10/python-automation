from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Bhoomika%20Agarwal/Desktop/Exercise%20Files/CH02/html_code_02.html")
content = driver.find_element_by_class_name('content')
print("My class element is:")
print(content)
driver.close()
