import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

link = 'http://suninjuly.github.io/math.html'
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get(link)
time.sleep(5)

people_radio = driver.find_element(By.ID, "peopleRule")

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

robots_radio = driver.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of people radio: ", robots_checked)
assert robots_checked is not None, "Robot radio is not selected by default"

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
