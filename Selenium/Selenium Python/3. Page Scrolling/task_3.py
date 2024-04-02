from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

DIV = ('xpath', '//div[@id="scroll-container"]/div')
SCROLL_CONTAINER = ('xpath', '//div[@id="scroll-container"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/infiniti_scroll_2/')

    for i in range(100):
        actions \
            .move_to_element(wait.until(EC.presence_of_element_located(DIV))) \
            .scroll_by_amount(0, 1) \
            .pause(1) \
            .perform()

    numbers = wait.until(EC.presence_of_element_located(SCROLL_CONTAINER)).text
    result = sum(int(number) for number in numbers.split())
    print(f'Result: {result}')