from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import title_is

class UserInfo:
    username = "tomsmith"
    password = "SuperSecretPassword!"

# Open Web Session on Firefox
driver = (webdriver.Firefox())
driver.get('https://the-internet.herokuapp.com/')

# Print Website Title
title = driver.title
print(title)

# Navigate to /login
formLink = driver.find_element(By.LINK_TEXT, 'Form Authentication')
formLink.click()

# Finds username and password names and fill them
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys(UserInfo.username)
password.send_keys(UserInfo.password)

# Click Login
login = driver.find_element(By.CSS_SELECTOR, 'i.fa-sign-in')
login.click()
logout = driver.find_element(By.CSS_SELECTOR, 'i.icon-signout')
logout.click()
# session.quit()
