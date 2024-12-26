from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

driver.get('https://www.youtube.com')

search = driver.find_element(By.CLASS_NAME, 'ytSearchboxComponentInput') #!!!

search.send_keys("HELLO SHITHEADS")
search.send_keys(Keys.ENTER)

breakpoint()