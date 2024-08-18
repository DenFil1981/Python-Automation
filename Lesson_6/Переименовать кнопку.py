from selenium import webdriver
#from time import sleep

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

button_name = driver.find_element(
    "id", "newButtonName").send_keys("Sky Pro")
#sleep(5)
confirm_button_name = driver.find_element("id", "updatingButton").click()
#sleep(5)
new_button_name = driver.find_element("id", "updatingButton").text 
#sleep(5)
print(new_button_name)

driver.quit()