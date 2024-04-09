from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

SLIDER = ('xpath', '//input[@class="volume-slider"]')
RESULT = ('xpath', '//p[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.10/6/index.html')

    sliders = wait.until(EC.visibility_of_any_elements_located(SLIDER))
    for i, slider in enumerate(sliders, start=1):
        current_value = int(slider.get_attribute('value'))
        target_value = int(
            wait.until(
                EC.visibility_of_element_located(
                    ('xpath', f'//div[@class="slider-container"][{i}]/span[@class="target-value"]')
                )
            ).text
        )
        while current_value != target_value:
            if current_value > target_value:
                slider.send_keys(Keys.ARROW_LEFT)
                current_value -= 1
            else:
                slider.send_keys(Keys.ARROW_RIGHT)
                current_value += 1

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
