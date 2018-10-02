from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Bhoomika/python-automation/Exercise%20Files/html_code_01.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()
