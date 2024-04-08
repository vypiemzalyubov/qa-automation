from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

CLICK_BTN = ('xpath', '//button[@id="btn"]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/expectations/3/index.html')

    wait.until(EC.element_to_be_clickable(CLICK_BTN)).click()
    if wait.until(EC.title_is('345FDG3245SFD')):
        result = wait.until(EC.visibility_of_element_located(RESULT)).text
        print(f'Result: {result}')
