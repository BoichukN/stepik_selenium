import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    out = calc(x)

    browser.find_element_by_id('answer').send_keys(out)

    browser.find_element_by_id('robotCheckbox').click()

    radio = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()

    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(3)
    browser.quit()
