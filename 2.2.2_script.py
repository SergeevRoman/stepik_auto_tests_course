import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

name = browser.find_element(By.CSS_SELECTOR,'input:nth-child(2)')
name.send_keys('Roman')

last_name = browser.find_element(By.CSS_SELECTOR,'input:nth-child(4)')
last_name.send_keys('Sergeev')

email = browser.find_element(By.CSS_SELECTOR,'input:nth-child(6)')
email.send_keys('s@s.we')


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


file = browser.find_element(By.ID, 'file')
file.send_keys(file_path)

button = browser.find_element(By.TAG_NAME,"button")
button.click()

time.sleep(5)
browser.quit()


