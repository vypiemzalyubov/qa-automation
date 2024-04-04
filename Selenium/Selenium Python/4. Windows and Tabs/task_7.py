from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BTN = ('xpath', '//input[@type="button"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/blank/3/index.html')

    result = 0

    button_list = wait.until(EC.visibility_of_all_elements_located(BTN))
    for i, button in enumerate(button_list, start=1):
        button.click()
        driver.window_handles
        driver.switch_to.window(driver.window_handles[i])
        result += int(driver.title)
        driver.switch_to.window(driver.window_handles[0])

    print(f'Result: {result}')
