from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BTN = ('xpath', '//button[@class="timer_button"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.7/5/index.html')

    button_list = wait.until(EC.visibility_of_all_elements_located(BTN))
    for button in button_list:
        value = button.get_attribute('value')
        actions \
            .click_and_hold(button) \
            .pause(float(value)) \
            .release(button) \
            .perform()

    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f'Result: {alert_text}')
