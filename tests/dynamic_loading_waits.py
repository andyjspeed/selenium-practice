from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Web Session on Firefox
driver = (webdriver.Firefox())
driver.get('https://the-internet.herokuapp.com/')

# Navigate to the Dynamic Loading Page using links.
formLink = driver.find_element(By.LINK_TEXT, 'Dynamic Loading')
formLink.click()

# Starting Example 1 Test
example1 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Example 1')
example1.click()
startbutton = driver.find_element(By.CSS_SELECTOR, 'button')
startbutton.click()
# Wait for Example 1 Test
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
print(element.text)
driver.back()


# Starting Example 2 Test
example2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Example 2')
example2.click()
startbutton = driver.find_element(By.CSS_SELECTOR, 'button')
startbutton.click()
# Wait for Example 2 Test
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'finish')))
print(element.text)
# driver.quit()