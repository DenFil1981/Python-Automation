from selenium.webdriver.common.by import By
from configuration import *

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("sesret_sauce")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "user_name").send_keys("standard_user")