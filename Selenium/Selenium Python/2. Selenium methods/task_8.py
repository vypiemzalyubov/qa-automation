import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

TEXTAREA_GRAY = ('xpath', '//textarea[@color="gray"]')
CHECK_BTN = ('xpath', '//button[@id="checkAll"]')
CONGRATS_FIELD = ('xpath', '//p[@id="congrats"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.5/4/1.html')

    textareas = wait.until(EC.visibility_of_all_elements_located(TEXTAREA_GRAY))
    for i, textarea in enumerate(textareas, start=1):
        wait.until(
            EC.visibility_of_element_located(('xpath', f'//div[@class="parent"][{i}]//textarea[@color="blue"]'))
        ).send_keys(textarea.text)
        textarea.clear()
        wait.until(EC.visibility_of_element_located(('xpath', f'//div[@class="parent"][{i}]//button'))).click()

    wait.until(EC.element_to_be_clickable(CHECK_BTN)).click()
    result = wait.until(EC.presence_of_element_located(CONGRATS_FIELD)).text
    print(f'Result: {result}')
