from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')


with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/methods/3/index.html')

    result = 0

    cookies = driver.get_cookies()
    for cookie in cookies:
        if 'secret_cookie' in cookie['name']:
            result += int(cookie['value'])

    print(f'Result: {result}')
