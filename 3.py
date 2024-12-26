from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get('https://www.kupibilet.ru/mbooking/step1/c21ed9b9-9d0d-4595-897b-53a997e3fdab')

# email

wait = WebDriverWait(driver, 10)
email_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='email-input']"))
)

email_input.click()
email_input.send_keys("123@gmail.com")

print("mail done.")

# phone

phone_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='phone-input']"))
)

phone_input.click()
phone_input.send_keys("87787742289")

print("entered phone number.")

# passport

doc_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='passport-input']"))
)

doc_input.click()
doc_input.send_keys("abcdefGO")

print("entered passport.")

# passport date

day_input = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passengers[0].passportExpdateDay']"))
)
day_input.click()
day_input.send_keys("28")


month_input = wait.until(EC.visibility_of_element_located((By.NAME, "passengers[0].passportExpdateMonth")))# wait till interactable
month_input.click()  

june_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Июнь']")))
june_option.click()

year_input = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passengers[0].passportExpdateYear']"))
)
year_input.click()
year_input.send_keys("2026")

# surname / name

surname_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='lastname-input']"))
)

surname_input.click()
surname_input.send_keys("Baurzhanov")

name_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='firstname-input']"))
)

name_input.click()
name_input.send_keys("Sultan")

# date of birth

day1_input = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passengers[0].birthdayDay']"))
)
day1_input.click()
day1_input.send_keys("28")


month1_input = wait.until(EC.visibility_of_element_located((By.NAME, "passengers[0].birthdayMonth")))# wait till interactable
month1_input.click()  

june1_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Июнь']")))
june1_option.click()

year1_input = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='passengers[0].birthdayYear']"))
)
year1_input.click()
year1_input.send_keys("2004")

# Print success message
print("Successfully selected the date 28th June 2004.")

# gender

male_gender_toggle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="gender-toggler-item-m"]')))
male_gender_toggle.click()

print('Selected gender')

# no baggage

no_baggage = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Без дополнительного багажа']")))
no_baggage.click()

print('No baggage')

# continue 

continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Продолжить']")))
continue_button.click()

print('Continuing...')

breakpoint()

driver.quit()