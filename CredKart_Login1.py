import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()
# Go to Url
driver.get("https://automation.credence.in/login")

# Enter email
# XPATH--> XPATH(XML Path Language) is used language to select elements
# or attribute from HTML pages
# XPATH Format --> //tagname[@attribute='value']
# Email Xpath --> //input[@type='email']
# To check Xpath in browser console --> $x("Xpath")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

# Enter Password
# CSS--> CSS(Cascading style sheets) is language used to describe
# presentation of HTML pages.
# CSS define visual properties of element like front, front size, colour, layout
# CSS format --> tagname[attribute='value']
# password css --> input[id='password']
# To check CSS in browser console --> $$("CSS")
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@1234")

# Click Login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# driver.title == "CredKart" -- > best practice
# Verify Login status
try:
    driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    print("Login TestCase is Passed")
except:
    print("Login TestCase is Failed")


driver.close()



# TestCase Studio
# SelectorHub