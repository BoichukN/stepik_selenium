import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    span_element = browser.find_element_by_id('input_value')
    span_text = span_element.text
    y = calc(span_text)
    browser.find_element_by_id('answer').send_keys(str(y))

    # Отметить checkbox "I'm the robot".
    browser.find_element_by_id('robotCheckbox').click()

    # Выбрать radiobutton "Robots rule!".
    browser.find_element_by_id('robotsRule').click()

    # Нажать на кнопку Submit.
    browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
