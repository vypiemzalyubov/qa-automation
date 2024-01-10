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

BASE_URL = "https://demoqa.com/selectable"
GO_TO_GRID = ("xpath", "//a[text()='Grid']")
ONE_BUTTON = ("xpath", "//li[text()='One']")
TWO_BUTTON = ("xpath", "//li[text()='Two']")


print("Start test")

driver.get(BASE_URL)

wait.until(EC.element_to_be_clickable(GO_TO_GRID)).click()

wait.until(EC.element_to_be_clickable(ONE_BUTTON)).click()
assert "active" in wait.until(EC.element_to_be_clickable(ONE_BUTTON)).get_attribute("class"), \
    "Element \"One\" is not selected"

wait.until(EC.element_to_be_clickable(TWO_BUTTON)).click()
assert "active" in wait.until(EC.element_to_be_clickable(TWO_BUTTON)).get_attribute("class"), \
    "Element \"Two\" is not selected"

wait.until(EC.element_to_be_clickable(ONE_BUTTON)).click()
assert "active" not in wait.until(EC.element_to_be_clickable(ONE_BUTTON)).get_attribute("class"), \
    "Element \"One\" is not selected, but should not be"

wait.until(EC.element_to_be_clickable(TWO_BUTTON)).click()
assert "active" not in wait.until(EC.element_to_be_clickable(TWO_BUTTON)).get_attribute("class"), \
    "Element \"Two\" is not selected, but should not be"

print("Finish test")
