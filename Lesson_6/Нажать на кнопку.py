from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.1)

driver.get("http://uitestingplayground.com/ajax") 

blue_button= driver.find_element(By.CSS_SELECTOR,"#ajaxButton").click()
text_from_content = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR,"p.bg-success"))).text

print(text_from_content)

driver.quit()


