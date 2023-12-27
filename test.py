from selenium import webdriver

driver = webdriver.Chrome()

vk_url = "https://vk.com/"
ya_url = "https://ya.ru/"
vk_title = "ВКонтакте | Добро пожаловать"

driver.get(vk_url)
PAGE_TITLE_VK = driver.title
print("Page Title: ", PAGE_TITLE_VK)

driver.get(ya_url)
PAGE_TITLE_YA = driver.title
print("Page Title: ", PAGE_TITLE_YA)

driver.back()
PAGE_TITLE = driver.title
assert vk_title == PAGE_TITLE, f"The page title should be {vk_title}. Current title: {PAGE_TITLE}"

driver.refresh()
PAGE_URL = driver.current_url
print("Page URL: ", PAGE_URL)

driver.forward()
NEW_PAGE_URL = driver.current_url
assert ya_url == NEW_PAGE_URL, f"The page URL should be {ya_url}. Current URL: {NEW_PAGE_URL}"
