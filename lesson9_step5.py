from selenium import webdriver

link = ''

browser = webdriver.Chrome()
browser.get(link)

# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window:
window_name = ''
browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
# который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки,
# выбираем вторую вкладку:
new_window = browser.window_handles[1]

# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
first_window = browser.window_handles[0]

