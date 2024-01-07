from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("--ignore-certificate-errors")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get("https://demoqa.com/dynamic-properties")

# VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
# wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)).click()

# VISIBLE_IN_SECONDS = ("xpath", "//button[@id='enableAfter']")
# wait.until(EC.element_to_be_clickable(VISIBLE_IN_SECONDS)).click()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
driver.find_element(*REMOVE_BUTTON).click()
wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
print("OK")

ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
TEXT = ("xpath", "//input[@type='text']")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(TEXT, "Hello"))
print("OK")