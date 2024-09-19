from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson_7.constants import Calculator_URL
import allure

class CalcMain:
    @allure.step("Открываем страницу калькулятора")
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Calculator_URL)
        
    @allure.step("Ищем поле ввода времени,очищаем значение и вводим новое")    
    def insert_time(self):
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)
        
    @allure.step("Вводим значения на калькуляторе")   
    def clicking_buttons(self):
        
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '=']").click()
    
    @allure.step("Ожидаем результат и вычисления и передаём в текстовом формате")    
    def wait_button_gettext(self):
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element(By.CLASS_NAME, "screen")) 
        return self.browser.find_element(By.CLASS_NAME, "screen").text   
                
