from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

OPTION = ('xpath', '//option')
INPUT_FIELD = ('xpath', '//input[@id="input_result"]')
SUBMIT_BTN = ('xpath', '//input[@id="sendbutton"]')
RESULT = ('xpath', '//input[@id="sendbutton"]/../following-sibling::*')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/7/7.html')

    options = wait.until(EC.visibility_of_all_elements_located(OPTION))
    options_value = sum([int(option.text) for option in options])

    wait.until(EC.visibility_of_element_located(INPUT_FIELD)).send_keys(options_value)
    wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
