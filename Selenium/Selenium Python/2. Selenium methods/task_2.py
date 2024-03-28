import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

INPUT = ('xpath', '//input[@type="text"]')
SUBMIT_BTN = ('xpath', '//button[@id="checkButton"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.5/1/1.html')

    input_fields = wait.until(EC.visibility_of_all_elements_located(INPUT))
    for field in input_fields:
        field.clear()

    wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()
    
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f'Result: {alert_text}')
