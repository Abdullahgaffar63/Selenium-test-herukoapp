from selenium import webdriver
from selenium.webdriver.chrome.service import Service   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service= Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/") 
driver.maximize_window()   

driver.find_element(By.PARTIAL_LINK_TEXT,"Form Authentication").click()

user="tomsmith"
passworf="SuperSecretPassword!"

INPUT= driver.find_element(By.ID,"username")
INPUT.clear()
INPUT.send_keys(user)
INPUTPASS=driver.find_element(By.ID,"password")
INPUTPASS.clear()
INPUTPASS.send_keys(passworf,Keys.ENTER)
time.sleep(3)
#driver.refresh()
time.sleep(20)
driver.quit()
