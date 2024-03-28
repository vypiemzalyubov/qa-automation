from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

LINK = ('xpath', '//a')
TEXT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/methods/5/index.html')

    cookie_dict = {}

    links = wait.until(EC.visibility_of_all_elements_located(LINK))
    for link in links:
        link.click()
        expiry = driver.get_cookies()[0]['expiry']
        text = wait.until(EC.visibility_of_element_located(TEXT)).text
        cookie_dict[text] = expiry
        driver.back()

    result = sorted(cookie_dict.items(), key=lambda x: x[1], reverse=True)[0][0]
    print(f'Result: {result}')
