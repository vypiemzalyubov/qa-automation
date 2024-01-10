import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Selenium")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

BASE_URL = "http://the-internet.herokuapp.com/checkboxes"

driver.get(BASE_URL)

CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

# # Выполняем клик по первому чек-боксу
# driver.find_element(*CHECKBOX_1).click()
# # Убеждаемся что первый чек-бокс действительно выставлен
# assert driver.find_element(*CHECKBOX_1).get_attribute("checked") is not None
# # Выполняем клик по второму чек-боксу
# driver.find_element(*CHECKBOX_2).click()
# # Убеждаемся что второй чек-бокс действительно не выставлен
# assert driver.find_element(*CHECKBOX_2).get_attribute("checked") is None

# Ставим флажок
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"

# Убираем флажок
driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"