from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

ALERT = ('xpath', '//button[@class="alert_button"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')

    for i in range(1, 101):
        actions \
            .move_to_element(
                wait.until(EC.presence_of_element_located(('xpath', f'//div[@class="child_container"][{i}]')))
            ) \
            .scroll_by_amount(0, 10) \
            .pause(1) \
            .perform()

        checkboxes = wait.until(
            EC.presence_of_all_elements_located(('xpath', f'//div[@class="child_container"][{i}]/input'))
        )
        for checkbox in checkboxes:
            if int(checkbox.get_attribute('value')) % 2 == 0:
                checkbox.click()

    wait.until(EC.presence_of_element_located(ALERT)).click()
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f'Result: {alert_text}')
