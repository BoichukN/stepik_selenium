import os
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

with open('test.txt', 'w') as t:
    t.write('Test text.')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('test')
    browser.find_element_by_name('lastname').send_keys('test')
    browser.find_element_by_name('email').send_keys('test@test.com')

    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_css_selector('button[type="submit"]').click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    time.sleep(3)
    browser.quit()
