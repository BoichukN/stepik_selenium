import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'


def calc(x : str, y : str):
    return str(int(x) + int(y))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1')
    y = browser.find_element_by_id('num2')

    out = calc(x.text, y.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(out)

    browser.find_element_by_css_selector("button.btn").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    time.sleep(5)
    browser.quit()
