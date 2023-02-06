import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import math

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)


link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get(link2)
time.sleep(2)

select = Select(driver.find_element(By.TAG_NAME,'select'))
select.select_by_value(str(int(driver.find_element(By.ID, "num1").text) + int(driver.find_element(By.ID, "num2").text)))

button = driver.find_element(By.CLASS_NAME, 'btn-default')
button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
