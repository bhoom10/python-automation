from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Bhoomika/python-automation/Exercise%20Files/html_code_01.html")
username = driver.find_element_by_name('username')
print("My input element is:")
print(username)
driver.close()
