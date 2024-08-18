from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()

try:
    # 1. Откройте страницу
    driver.get('http://the-internet.herokuapp.com/login')

    # 2. В поле username введите значение tomsmith
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys('tomsmith')

    # 3. В поле password введите значение SuperSecretPassword!
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('SuperSecretPassword!')

    # 4. Нажмите кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # Опционально: Подождите несколько секунд, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закройте браузер
    driver.quit()