import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

standart_login = 'standard_user'  # логин для входа
password_all = 'secret_sauce'  # пароль для входа

driver.maximize_window()
# user_name = driver.find_element(by=By.ID, value="user-name") # ID
# user_name =driver.find_element(by=By.XPATH, value = "//*[@id='user-name']") #XPATH

user_name = driver.find_element(by=By.XPATH,
                                value="//input[@data-test='username']")  # тоже XPATH но ищу по конекретному элементу в в коде (ищу data-test='username')
user_name.send_keys(standart_login)
print("Input Login")
time.sleep(0.5)

password = driver.find_element(by=By.CSS_SELECTOR,
                               value="#password")  # Вводим пароль (необязательно через CSS_Selector)
password.send_keys(password_all)
print("Input PassWord")
time.sleep(0.5)

button_login = driver.find_element(by=By.XPATH, value="//*[@id='login-button']")  # кликаем на кнопку Login
button_login.click()
print("Click Login Button")

text_products = button_login = driver.find_element(by=By.XPATH, value="//*[@id='header_container']/div[2]/span")
value_text_products = text_products.text  # считываем текст из логотипа на сайте
print(f"Логотип страницы после авторизации: {value_text_products}")
assert value_text_products == "Products"  # проверка, на правильную ли страницу происходит перенос при авторизации по названию логотипа

get_url = driver.current_url
real_url = "https://www.saucedemo.com/inventory.html"  # нужный url после авторизации
print(f"Перешли на страницу: {get_url}")
assert get_url == real_url
time.sleep(1)

# далее кусок кода по созданию скриншота с привязкой даты в названии
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = "screenshot" + now_date
driver.save_screenshot(f".\\screen\\screenshot {name_screenshot}.png")
print(name_screenshot)
time.sleep(3)
