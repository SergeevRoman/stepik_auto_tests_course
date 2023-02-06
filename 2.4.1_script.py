import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), '$100')
    )
button = browser.find_element(By.ID, "book")    
button.click()

value = int(browser.find_element(By.ID, "input_value").text)

answer = calc(value)

fanswer = browser.find_element(By.ID, 'answer')
fanswer.send_keys(answer)

button = browser.find_element(By.ID,"solve")
button.click()

time.sleep(5)
browser.quit()



