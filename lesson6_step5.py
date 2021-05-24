import math
import time

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/find_link_text')

link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

input1 = browser.find_element_by_tag_name('input')
input1.send_keys("Natalia")
input2 = browser.find_element_by_name('last_name')
input2.send_keys("Boichuk")
input3 = browser.find_element_by_class_name('city')
input3.send_keys("Lviv")
input4 = browser.find_element_by_id('country')
input4.send_keys("Ukraine")
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(30)
browser.quit()
