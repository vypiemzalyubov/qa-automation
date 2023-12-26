# 1. Иницализация в одну строчку, через SeleniumManager - он автоматически распознает ваш Chrome и запустит его. 
# Но важно перед этим найти у себя на компьютере через поиск chromedriver.exe и удалить его!

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demoqa.com/forms")

PAGE_URL = driver.current_url

print(PAGE_URL)

PAGE_TITLE = driver.title

print("Title страницы: ", PAGE_TITLE)

PAGE_SOURCE = driver.page_source

print(PAGE_SOURCE)