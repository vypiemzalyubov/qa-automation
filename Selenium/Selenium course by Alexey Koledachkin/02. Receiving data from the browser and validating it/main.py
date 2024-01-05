from selenium import webdriver

driver = webdriver.Chrome()

VK_URL = "https://vk.com/"
YA_URL = "https://ya.ru/"
VK_TITLE = "ВКонтакте | Добро пожаловать"

driver.get(VK_URL)
page_title_vk = driver.title
print("Page Title: ", page_title_vk)

driver.get(YA_URL)
page_title_ya = driver.title
print("Page Title: ", page_title_ya)

driver.back()
page_title = driver.title
assert VK_TITLE == page_title, f"The page title should be {VK_TITLE}. Current title: {page_title}"

driver.refresh()
page_url = driver.current_url
print("Page URL: ", page_url)

driver.forward()
new_page_url = driver.current_url
assert YA_URL == new_page_url, f"The page URL should be {YA_URL}. Current URL: {new_page_url}"
