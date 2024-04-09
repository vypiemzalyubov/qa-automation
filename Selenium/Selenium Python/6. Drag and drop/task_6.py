import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BALLS = ('xpath', '//div[contains(@class, "ball_color")]')
RESULT = ('xpath', '//p[@class="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.10/4/index.html')

    for ball in wait.until(EC.visibility_of_any_elements_located(BALLS)):
        color = ball.get_attribute('class').split()[1].replace('_ball', '')
        target = wait.until(
            EC.visibility_of_element_located(('xpath', f'//div[contains(@class, "basket_color {color}")]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", ball)
        actions.drag_and_drop(ball, target).perform()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
