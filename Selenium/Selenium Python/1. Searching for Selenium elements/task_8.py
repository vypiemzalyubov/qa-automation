from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

TEXT_BOX = ('xpath', '//div[@id="text_box"]')
SELECT = ('xpath', '//select[@id="selectId"]')
SUBMIT_BTN = ('xpath', '//input[@id="sendbutton"]')
RESULT = ('xpath', '//input[@id="sendbutton"]/../following-sibling::*')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/6/6.html')

    text_box_values = wait.until(EC.visibility_of_all_elements_located(TEXT_BOX))
    values = [value.text for value in text_box_values]
    value = eval(*values)

    wait.until(EC.visibility_of_element_located(SELECT)).send_keys(value)
    wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
