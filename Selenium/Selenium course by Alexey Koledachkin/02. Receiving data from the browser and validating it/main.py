from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://vk.com/")
PAGE_TITLE_VK = driver.title
print("Page Title: ", PAGE_TITLE_VK)

driver.get("https://ya.ru/")
PAGE_TITLE_YA = driver.title
print("Page Title: ", PAGE_TITLE_YA)

driver.back()
PAGE_TITLE = driver.title
assert "ВКонтакте | Добро пожаловать" == PAGE_TITLE, f"The page title should be \"ВКонтакте | Добро пожаловать\". Current title: {PAGE_TITLE}"

driver.refresh()
PAGE_URL = driver.current_url
print("Page URL: ", PAGE_URL)

driver.forward()
NEW_PAGE_URL = driver.current_url
assert "https://ya.ru/" == NEW_PAGE_URL, f"The page URL should be \"https://ya.ru/\". Current URL: {NEW_PAGE_URL}"
