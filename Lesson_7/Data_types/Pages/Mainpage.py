from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_7.constants import Test_form_URL
from lesson_7.Data_types import *

class MainPage:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.browser.get(Test_form_URL)
        
        
    def find_fields(self):
        self._first_name = (By.NAME, "first_name")  
        self._last_name = (By.NAME, "last_name")
        self._aadress = (By.NAME, "aadress")
        self._email = (By.NAME, "email")
        self._phone = (By.NAME, "phone")
        self._zip_code = (By.NAME, "zip_code")
        self._city = (By.NAME, "city")
        self._country = (By.NAME, "country" )
        self._job_position = (By.NAME, "job_position")
        self._company = (By.NAME, "company")
        self._button = (By.NAME, "button")
        
    def filling_in_the_fields(self):
        self.browser.find_element(*self._first_name).send_keys(first_name)
        self.browser.find_element(*self._last_name).send_keys(last_name)
        self.browser.find_element(*self._aadress).send_keys(aadress)
        self.browser.find_element(*self._email).send_keys(email)
        self.browser.find_element(*self._phone).send_keys(phone)
        self.browser.find_element(*self._zip_code).send_keys(zip_code)
        self.browser.find_element(*self._city).send_keys(city)
        self.browser.find_element(*self._country).send_keys(country)
        self.browser.find_element(*self._job_position).send_keys(job_position)
        self.browser.find_element(*self._company).send_keys(company)
        
    def click_submit_button(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()
        