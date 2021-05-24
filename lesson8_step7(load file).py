import os

from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')    # добавляем к этому пути имя файла

link = 'http/'
browser = webdriver.Chrome()
browser.get(link)
element = browser.find_element_by_id('answer')
element.send_keys(file_path)
