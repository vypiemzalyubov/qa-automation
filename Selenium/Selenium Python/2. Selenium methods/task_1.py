from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/methods/1/index.html')

    default_text = wait.until(EC.visibility_of_element_located(RESULT)).text

    while True:
        result = wait.until(EC.visibility_of_element_located(RESULT)).text
        if result != default_text:
            print(f'Result: {result}')
            break
        driver.refresh()
