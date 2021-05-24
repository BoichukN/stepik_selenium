from selenium import webdriver

link = ''
browser = webdriver.Chrome()
browser.get(link)


browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()

# from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1")
# select.select_by_visible_text("text")
# select.select_by_index(index)
