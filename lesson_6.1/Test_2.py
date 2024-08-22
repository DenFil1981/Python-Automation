from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *

def test_calculator_form(Chrome_browser):
    Chrome_browser.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = Chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    
    
    Chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    Chrome_browser.find_elemen(By.XPATH, "//span[text() = '+']").click()
    Chrome_browser.find_elemen(By.XPATH, "//span[text() = '8']").click()
    Chrome_browser.find_elemen(By.XPATH, "//span[text() = '=']").click()
    
    WebDriverWait(Chrome_browser, 46).until (EC. text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    
    result_text = Chrome_browser.find_element(By.CLASS_NAME, "screen").text
    
    assert result_text == "15"
    