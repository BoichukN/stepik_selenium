from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Natalia")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Boichuk")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Lviv")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Ukraine")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()