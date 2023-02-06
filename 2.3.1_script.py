import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME,"button")
button.click()

time.sleep(2)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_value = int(browser.find_element(By.ID,'input_value').text)

value = calc(x_value)

form = browser.find_element(By.CLASS_NAME,'form-control')

form.send_keys(value)

button = browser.find_element(By.TAG_NAME,"button")
button.click()

time.sleep(5)
browser.quit()


