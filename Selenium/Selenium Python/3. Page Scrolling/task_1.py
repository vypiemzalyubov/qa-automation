from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

CHECKBOX = ('xpath', '//input[@type="checkbox"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/scroll/2/index.html')

    result = 0

    checkboxes = wait.until(EC.visibility_of_all_elements_located(CHECKBOX))
    for i, checkbox in enumerate(checkboxes, start=1):
        checkbox.click()
        span_text = wait.until(EC.presence_of_element_located(('xpath', f'//div[@class="item"][{i}]//span'))).text
        if span_text:
            result += int(span_text)

    print(f'Result: {result}')
