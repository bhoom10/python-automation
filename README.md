
# python-automation
A short tutorial to automate web UI testing with Python and Selenium 

## Installation
1. [Download python](https://www.python.org/downloads/)
2. [Download Python Selenium bindings](https://selenium-python.readthedocs.io/installation.html)
3. [Download drivers for your favorite browser](https://selenium-python.readthedocs.io/installation.html#drivers)

## Contents
1. What is automated testing?
2. Python Selenium bindings
3. Parsing the DOM structure
4. Locating elements in the HTML DOM
5. Navigating through pages
6. Waits

## Exercise 0: Test your setup

Once you have installed python, python-selenium bindings and the web driver, let's test if the setup is complete 

	    from selenium import webdriver
        import time
        driver= webdriver.Chrome()
        driver.get('http://seleniumhq.org')
        time.sleep(2)
        driver.close()

##  Exercise 1: Locating elements by ID
 - Download the file *html_code_01*
 - Use the path of this file in your
   automation script and locate the element by ID *loginForm*

## Exercise 2: Locating elements by name
 - Download the file *html_code_01*
 - Use the path of this file in your
   automation script and locate the element by name *username*

## Exercise 3: Locating elements by xpath
 - Download the file *html_code_01*
 - Use the path of this file in your
   automation script and locate the login form element using relative xpath, absolute xpath and using xpath with an attribute

## Exercise 4: Locate elements by class name
 - Download the file *html_code_01*
 - Use the path of this file in your
   automation script and locate the element by class name *content*

## Challenge 1: Locate elements in the DOM
1. Go to http://www.seleniumhq.org/
2. Locate the element by id *q*
3. Locate the element by name *q*
4. Locate the element heading *What is Selenium?* by xpath 
5. Find element by class *selenium-sponsors*

## Exercise 5: Perform a simple search
 - Navigate to http://python.org
 - Find the search bar 
 - Perform a search for *pycon*

## Exercise 6: 
 - Download the file *html_code_02*
 - Use the path of this file in your automation script 
 - Locate the select element by name *numReturnSelect* and select values by index, visible text and value
- Submit the selection made

 ## Exercise 7: Drag and Drop
 - Navigate to http://jqueryui.com/droppable
 - Use ActionChains to drag and drop elements by offset or from a source to a target 
 
## Challenge 2: Navigate through a web page
1. Go to https://wiki.python.org/moin/FrontPage
2. Perform a Search for the text *Beginner* 
3. In the left side menubar, change the value of the select from 'More Options' to 'Raw Text'

## Exercise 8: Explicit wait
- Navigate to http://www.python.org
- Add an explicit wait of 10 seconds for the element with id *start-shell*

## Exercise 9: Implicit wait
-  Navigate to http://www.python.org
- Add an implicit wait of 10 seconds for the element with id *start-shell*