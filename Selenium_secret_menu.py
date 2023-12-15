import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

standart_login = 'standard_user' # логин для входа
password_all = 'secret_sauce' # пароль для входа

driver.maximize_window()
# user_name = driver.find_element(by=By.ID, value="user-name") # ID
# user_name =driver.find_element(by=By.XPATH, value = "//*[@id='user-name']") #XPATH

# тоже XPATH но ищу по конекретному элементу в в коде (ищу data-test='username')
user_name = driver.find_element(by=By.XPATH,
                                value="//input[@data-test='username']")
user_name.send_keys(standart_login)
print("Input Login")
time.sleep(0.5)

# Вводим пароль (необязательно через CSS_Selector)
password = driver.find_element(by=By.CSS_SELECTOR,
                               value="#password")
password.send_keys(password_all)
print("Input PassWord")
time.sleep(0.5)

# кликаем на кнопку Login
button_login = driver.find_element(by=By.XPATH, value="//*[@id='login-button']")
button_login.click()
print("Click Login Button")

text_products = driver.find_element(by=By.XPATH, value="//*[@id='header_container']/div[2]/span")
value_text_products = text_products.text # считываем текст из логотипа на сайте
print(f"Логотип страницы после авторизации: {value_text_products}")
assert value_text_products == "Products" # проверка, на правильную ли страницу происходит перенос при авторизации по названию логотипа

get_url = driver.current_url
real_url = "https://www.saucedemo.com/inventory.html" # нужный url после авторизации
print(f"Перешли на страницу: {get_url}")
assert get_url == real_url
time.sleep(1)

# кликаем на кнопку Меню
secret_menu = driver.find_element(by=By.XPATH, value='//*[@id="react-burger-menu-btn"]')
secret_menu.click()
print("Click Menu")
time.sleep(1)

# кликаем на кнопку About
menu_about = driver.find_element(by=By.XPATH, value="//*[@id='about_sidebar_link']")
menu_about.click()
print("Click About")
time.sleep(2)