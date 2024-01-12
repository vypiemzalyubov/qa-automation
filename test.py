import time
import platform
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Selenium")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

# BASE_URL = "http://the-internet.herokuapp.com/dropdown"
# DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")

# driver.get(BASE_URL)

# DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
# DROPDOWN.select_by_value("2")
# print(DROPDOWN.options)
# time.sleep(5)


# BASE_URL = "http://the-internet.herokuapp.com/key_presses"
# KEY_PRESS_INPUT = ("xpath", "//input[@id='target']")

# driver.get(BASE_URL)

# driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello World")
# time.sleep(2)
# driver.find_element(*KEY_PRESS_INPUT).send_keys(CMD_CTRL + "A")
# time.sleep(2)
# driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACKSPACE)
# time.sleep(2)


# BASE_URL = "https://clipboardjs.com/"
# PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")

# driver.get(BASE_URL)

# PASTE = driver.find_element(*PASTE_LOCATOR)

# PASTE.send_keys(CMD_CTRL + "A")
# time.sleep(2)
# PASTE.send_keys(CMD_CTRL + "X")
# time.sleep(2)
# PASTE.send_keys(CMD_CTRL + "V")
# time.sleep(2)

BASE_URL = "https://demoqa.com/select-menu"
SELECT_TITLE = ("xpath", "//input[@id='react-select-3-input']")

driver.get(BASE_URL)

# driver.find_element(*SELECT_TITLE).send_keys("Mrs.")
# driver.find_element(*SELECT_TITLE).send_keys(Keys.ENTER)
# time.sleep(2)

# driver.find_element("xpath", "//div[@id='withOptGroup']").click()
# time.sleep(2)
# driver.find_element("xpath", "//div[@id='withOptGroup']//div[text()='A root option']").click()
# time.sleep(2)

MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")

driver.find_element(*MULTISELECT).send_keys("Gre")

assert driver.find_element(*MULTISELECT).get_attribute("value") == "Gre", "Текст не введен"

driver.find_element(*MULTISELECT).send_keys(Keys.TAB)
time.sleep(2)