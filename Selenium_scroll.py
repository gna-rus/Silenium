import time
import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
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
time.sleep(0.5)

password = driver.find_element(by=By.CSS_SELECTOR,
                               value="#password")  # Вводим пароль (необязательно через CSS_Selector)
password.send_keys(password_all)
print("Input PassWord")
time.sleep(0.5)

# кликаем на кнопку Login
button_login = driver.find_element(by=By.XPATH, value="//*[@id='login-button']")
button_login.click()
print("Click Login Button")

time.sleep(1)
driver.execute_script("window.scroll(0,100)") # скроллинг окна вниз на 100 а в бок на 0 пикселей
time.sleep(1)

# скролим до определенного элемента
action = ActionChains(driver)
find_T_shirt = driver.find_element(by=By.XPATH, value="//*[@id='item_2_img_link']/img")
action.move_to_element(find_T_shirt).perform()
time.sleep(1)

now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = "screenshot" + now_date
driver.save_screenshot(f".\\screen\\screenshot {name_screenshot}.png")
print(name_screenshot)

time.sleep(3)
