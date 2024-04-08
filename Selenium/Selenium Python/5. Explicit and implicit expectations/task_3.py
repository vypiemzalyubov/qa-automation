from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

CLICK_BTN = ('xpath', '//button[@id="btn"]')
RESULT = ('xpath', '//div[@class="BMH21YY"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/expectations/6/index.html')

    wait.until(EC.element_to_be_clickable(CLICK_BTN)).click()
    result = wait.until(EC.presence_of_element_located(RESULT))
    if result:
        print(f'Result: {result.text}')
