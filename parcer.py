# Парсер для определения самого дешевого автомобиля LADA в кредит на сайте auto.ru
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import re


s = Service('C:/.../msedgedriver.exe')
browser = webdriver.Edge(service=s)
browser.maximize_window()
browser.get("http://auto.ru")

# Находим и нажимаем кнопку LADA
search_button_LADA = browser.find_element(By.CSS_SELECTOR, '[title="LADA (ВАЗ)"]')
search_button_LADA.click()

# Ждем загрузки страницы
time.sleep(5)

# Cтавим галочку в чекбокс "В кредит" и смотрим доступные предложения
check_box = browser.find_element(By.NAME, "on_credit").click()
show_suggestions = browser.find_element(By.CLASS_NAME, "ButtonWithLoader__content").click()

# Ждем загрузки страницы
time.sleep(5)

# Находим названия автомобилей и их цены
show_names = browser.find_elements(By.XPATH, "//a[@class='Link ListingItemTitle__link']")
show_prices = browser.find_elements(By.XPATH, "//div[@class='ListingItemPrice__content']")

# Нахождение модели самого дешевого автомобиля
the_cheapiest_model_name = ''
the_cheapiest_model_price = 10 ** 8
for name, price in zip(show_names, show_prices):
    price_int = re.sub(r"\D", "", price.text)
    print(f'\nЦена автомобиля: {price_int} рублей \nНазвание модели: {name.text}')
    if int(price_int) < the_cheapiest_model_price:
        the_cheapiest_model_price = int(price_int)
        the_cheapiest_model_name = name.text

print(f'\nСамый дешевый автомобиль: {the_cheapiest_model_name}, цена: {the_cheapiest_model_price} рублей')
browser.close()
