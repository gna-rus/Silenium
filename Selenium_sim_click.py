import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

standart_login = 'standard_user' # логин для входа
password_all = 'secret_sauce' # пароль для входа

driver.maximize_window()
# user_name = driver.find_element(by=By.ID, value="user-name") # ID
# user_name =driver.find_element(by=By.XPATH, value = "//*[@id='user-name']") #XPATH

user_name = driver.find_element(by=By.XPATH,
                                value="//input[@data-test='username']")  # тоже XPATH но ищу по конекретному элементу в в коде (ищу data-test='username')
user_name.send_keys(standart_login)
print("Input Login")
user_name.send_keys(Keys.BACKSPACE) # один раз нажимается BackSpace
time.sleep(1)
user_name.send_keys(Keys.BACKSPACE * 2) # два раза нажимается BackSpace
time.sleep(1)
user_name.send_keys("ser") # вводим буквы "er"

password = driver.find_element(by=By.CSS_SELECTOR,
                               value="#password")  # Вводим пароль (необязательно через CSS_Selector)
password.send_keys(password_all)
print("Input PassWord")
time.sleep(0.5)
password.send_keys(Keys.RETURN) # нажатие кнопки Enter

filter_prod = driver.find_element(by=By.XPATH, value= "//*[@id='header_container']/div[2]/div/span/select")
filter_prod.click()
print("Открыл фильтр")
time.sleep(0.5)
filter_prod.send_keys(Keys.DOWN) # Нажал на кнопку Dpwn
time.sleep(0.5)
filter_prod.send_keys(Keys.RETURN)

# button_login = driver.find_element(by=By.XPATH, value="//*[@id='login-button']") # кликаем на кнопку Login
# button_login.click()
# print("Click Login Button")


time.sleep(3)
