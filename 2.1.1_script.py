import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


import math

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get(link)
time.sleep(5)

treasure = driver.find_element(By.ID, "treasure")

value = treasure.get_attribute("valuex")

answer = calc(value)
print('ответ равен: ', answer)

input = driver.find_element(By.ID, "answer")

input.send_keys(answer)

robotCheckbox = driver.find_element(By.ID, 'robotCheckbox')
robotCheckbox.click()

robotsRule = driver.find_element(By.ID, 'robotsRule')
robotsRule.click()

button = driver.find_element(By.CLASS_NAME, 'btn-default')
button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
