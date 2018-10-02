from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Bhoomika%20Agarwal/Desktop/Exercise%20Files/CH02/html_code_02.html")
username = driver.find_element_by_name('username')
print("My input element is:")
print(username)
driver.close()
