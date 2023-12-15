import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

standart_login = 'standard_use' # не правильный логин для входа
password_all = 'secret_sauce' # пароль для входа

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

button_login = driver.find_element(by=By.XPATH, value="//*[@id='login-button']") # кликаем на кнопку Login
button_login.click()
print("Click Login Button")

warring = driver.find_element(by=By.XPATH, value="//*[@id='login_button_container']/div/form/div[3]/h3")
value_warring_text = warring.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print(value_warring_text)
print("Good test")
time.sleep(2)

driver.refresh() # обновить страницу

time.sleep(3)
