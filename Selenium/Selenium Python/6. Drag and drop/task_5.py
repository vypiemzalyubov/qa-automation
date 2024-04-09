from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BLANK_SQUARE = ('xpath', '//div[contains(@style, "background-color")]')
RESULT = ('xpath', '//p[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.10/3/index.html')

    dict_color = {
        'rgb(255, 0, 0)': 'red',
        'rgb(0, 128, 0)': 'green',
        'rgb(0, 0, 255)': 'blue',
        'rgb(255, 255, 0)': 'yellow',
        'rgb(128, 0, 128)': 'purple',
        'rgb(255, 165, 0)': 'orange',
        'rgb(255, 192, 203)': 'pink',
        'rgb(165, 42, 42)': 'brown',
        'rgb(128, 128, 128)': 'grey',
        'rgb(0, 255, 255)': 'cyan'
    }

    containers = wait.until(EC.visibility_of_any_elements_located(BLANK_SQUARE))
    for box in containers:
        color = Color.from_string(box.value_of_css_property('background-color')).rgb
        target = wait.until(
            EC.visibility_of_element_located(('xpath', f'//div[contains(@style, "border-color: {dict_color[color]}")]'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", box)
        actions.drag_and_drop(box, target).perform()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
