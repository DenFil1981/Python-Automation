from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class ShopContainer:
    @allure.step("Заходим в интернет магазине в 'Корзину'") 
    def __init__(self, browser):
        self.browser = browser
        
    @allure.step("Проверяем товары в 'Корзине'")    
    def checkout(self):
        self.check = (By.ID, "checkout")
        self.browser.find_element(*self.check).click()
    
    @allure.step("Заполняем данные и кликаем дальше")    
    def into(self):
        self.first_name = (By.ID, "first_name")
        self.browser.find_element(*self.first_name).send_keys("Den")
        self.last_name = (By.ID, "last_name")  
        self.browser.find_element(*self.last_name).send_keys("Filinov")
        self.postcode = (By.ID, "postal_code")
        self.browser.find_element(*self.postcode).send_keys("561500") 
        self.continue_button = (By.ID, "continue")
        self.browser.find_element(*self.continue_button).click() 
     
    @allure.step("Ожидаем окончательную цену покупки")    
    def price(self):
        WebDriverWait(self.browser, 10, 0.1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "total_price")))
        total_price = self.browser.find_element(By.CSS_SELECTOR, "summary_total_label")
        total =total_price.text.strip().replace("Total: $", "")
        return total        
    