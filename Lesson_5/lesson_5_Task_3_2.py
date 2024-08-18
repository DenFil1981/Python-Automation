from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка веб-драйвера 
driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Определяем синюю кнопку по её атрибуту или элементу
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

# Запускаем клик три раза
for _ in range(3):
    blue_button.click()
    time.sleep(1)  # Небольшая пауза между кликами

# Закрываем драйвер
driver.quit()