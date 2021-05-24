from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
# from selenium.webdriver.common.keys import Keys
# browser.find_element_by_tag_name('body').send_keys(Keys.END)
# или Home если наверх
