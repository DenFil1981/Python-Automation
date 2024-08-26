from selenium.webdriver.common.by import By
from configuration import *

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("seсret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrome_browser.find_element(By.ID, "shoping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()
    chrome_browser.find_element(By.ID, "first_name").send_keys("Den")
    chrome_browser.find_element(By.ID, "last_name").send_keys("Filinov")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("11413")
    chrome_browser.find_element(By.ID, "continue").click()
    total_price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total:$", "")
    
    excepted_total = "58.29"
    assert total == excepted_total
    print("Итоговая сумма равна $58.29")
    