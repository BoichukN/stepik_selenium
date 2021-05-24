import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    img_element = browser.find_element_by_css_selector('.form-group img')

    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = img_element.get_attribute('valuex')

    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    out_put = calc(x)

    # Ввести ответ в текстовое поле.
    browser.find_element_by_id('answer').send_keys(str(out_put))

    # Отметить checkbox "I'm the robot".
    # Выбрать radiobutton "Robots rule!".
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    # Нажать на кнопку "Submit".
    browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


finally:
    time.sleep(5)
    browser.quit()
