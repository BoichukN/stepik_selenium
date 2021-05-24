import math
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    browser.find_element_by_id('book').click()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    out = calc(x)

    browser.find_element_by_id('answer').send_keys(out)
    browser.find_element_by_id('solve').click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
finally:
    time.sleep(2)
    browser.quit()


