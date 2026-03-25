from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_is

# Open Web Session on Firefox
session = (webdriver.Firefox())
session.get('https://the-internet.herokuapp.com/')

# Print Website Title
title = session.title
print(title)

# Navigate to /login
formLink = session.find_element(By.LINK_TEXT, 'Form Authentication')
formLink.click()

# Finds username and password names and fill them
username = session.find_element(By.ID, 'username')
password = session.find_element(By.NAME, 'password')
username.send_keys('tomsmith')
password.send_keys('SuperSecretPassword')

# Click Login
login = session.find_element(By.CSS_SELECTOR, 'i')
login.click()
# session.quit()