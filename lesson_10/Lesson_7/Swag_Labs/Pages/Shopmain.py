from selenium.webdriver.common.by import By
from Lesson_7.constants import Shop_URL
import allure



class ShopmainPage:
    @allure.step("Проходим в онлайн магазин по ссылке")
    def __init__(self, browser) -> None:
        self.browser = browser
        self.browser.get(Shop_URL)
        
    @allure.step("Регистрируемся и заполняем поля данными")    
    def registration_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standart_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()
        
    @allure.step("Выбираем товары")   
    def buy_issue(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Bolt_Tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")  
    
    @allure.step("Добавляем с помощью клика товары")      
    def click_issue(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_Tshirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()
        
    @allure.step("Переходим в корзину")      
    def into_container(self):
        self.Container = (By.ID, "shopping_cart_container") 
        self.browser.find_element(*self.Container).click()         
            
           