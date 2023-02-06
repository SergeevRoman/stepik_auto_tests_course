import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)



value = int(browser.find_element(By.ID,'input_value').text)

answer = calc(value)

answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(answer)


button = browser.find_element(By.TAG_NAME,"button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)



robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
robotCheckbox.click()

robotsRule = browser.find_element(By.ID, 'robotsRule')
robotsRule.click()


button.click()
time.sleep(5)
browser.quit()


