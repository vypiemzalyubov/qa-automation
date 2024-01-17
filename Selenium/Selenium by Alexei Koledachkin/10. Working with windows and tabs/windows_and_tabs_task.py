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
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)


HYPERSKILL_URL = "https://hyperskill.org/login"
AVITO_URL = "https://www.avito.ru/"
VK_URL = "https://vk.com/"
HYPERSKILL_BUTTON = ("xpath", "//a[text()=' Reset password ']")
AVITO_BUTTON = ("xpath", "//a[text()='О компании']")
VK_BUTTON = ("xpath", "//a[text()='О ВКонтакте']")

driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")

tabs = driver.window_handles

print(20 * "*")
print("Start receiving page titles")
driver.switch_to.window(tabs[0])
driver.get(HYPERSKILL_URL)
print(f"First title: {driver.title}")

driver.switch_to.window(tabs[1])
driver.get(AVITO_URL)
print(f"Second title: {driver.title}")

driver.switch_to.window(tabs[2])
driver.get(VK_URL)
print(f"Third title: {driver.title}")
print("Finish receiving page titles")
print(20 * "*")

print(20 * "*")
print("Start clicking buttons")
driver.switch_to.window(tabs[0])
wait.until(EC.element_to_be_clickable(HYPERSKILL_BUTTON)).click()
assert driver.title == "Password Reset - Hyperskill", \
    "Invalid page title. Valid: Password Reset - Hyperskill"

driver.switch_to.window(tabs[1])
wait.until(EC.element_to_be_clickable(AVITO_BUTTON)).click()
assert driver.title == "Об Avito", \
    "Invalid page title. Valid: Об Avito"

driver.switch_to.window(tabs[2])
wait.until(EC.element_to_be_clickable(VK_BUTTON)).click()
assert driver.title == "ВКонтакте | Добро пожаловать", \
    "Invalid page title. Valid: ВКонтакте | Добро пожаловать"
print("Finish clicking buttons")
print(20 * "*")
