from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

INPUT = ('xpath', '//input[@type="text"]')
SUBMIT_BTN = ('xpath', '//button[@id="checkButton"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/methods/3/index.html')

    cookies = driver.get_cookies()

    result = sum([int(cookie['value']) for cookie in cookies if int(cookie['name'].split('_')[-1]) % 2 == 0])
    print(f'Result: {result}')
