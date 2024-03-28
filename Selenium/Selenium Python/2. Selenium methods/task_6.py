from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BUTTON = ('xpath', '//button[@class="btn"]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/scroll/4/index.html')

    result = 0

    buttons = wait.until(EC.visibility_of_all_elements_located(BUTTON))
    for button in buttons:
        driver.execute_script('return arguments[0].scrollIntoView(true);', button)
        button.click()
        result += int(wait.until(EC.presence_of_element_located(RESULT)).text)

    print(f'Result {result}')
