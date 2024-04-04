from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

CHECKBOX = ('xpath', '//input[@type="checkbox"]')
RESULT = ('xpath', '//span[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)

    result = 0

    sites = [
        'http://parsinger.ru/blank/1/1.html',
        'http://parsinger.ru/blank/1/2.html',
        'http://parsinger.ru/blank/1/3.html',
        'http://parsinger.ru/blank/1/4.html',
        'http://parsinger.ru/blank/1/5.html',
        'http://parsinger.ru/blank/1/6.html',
    ]
    for site in sites:
        driver.get(site)
        wait.until(EC.visibility_of_element_located(CHECKBOX)).click()
        result_text = wait.until(EC.visibility_of_element_located(RESULT)).text
        result += int(result_text) ** 0.5

    print(f'Result: {round(result, 9)}')
