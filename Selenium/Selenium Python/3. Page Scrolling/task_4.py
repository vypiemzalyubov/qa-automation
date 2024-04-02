from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')


with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/infiniti_scroll_3/')

    result = 0

    for i in range(1, 6):
        while True:
            actions \
                .move_to_element(
                    wait.until(EC.presence_of_element_located(('xpath', f'//div[@id="scroll-container_{i}"]/div')))
                ) \
                .scroll_by_amount(0, 100) \
                .pause(1) \
                .perform()
            try:
                driver.find_element(
                    'xpath', f'//*[@id="scroll-container_{i}"]//*[@class="last-of-list"]'
                )
                break
            except NoSuchElementException:
                pass

        numbers = wait.until(EC.presence_of_element_located(('xpath', f'//div[@id="scroll-container_{i}"]'))).text
        result += sum(int(number) for number in numbers.split())

    print(f'Result: {result}')
