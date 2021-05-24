import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    out = calc(x)

    browser.find_element_by_id('answer').send_keys(out)
    browser.find_element_by_tag_name('button').click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
finally:
    time.sleep(3)
    browser.quit()
