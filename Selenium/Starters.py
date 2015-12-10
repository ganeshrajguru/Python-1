from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8080')
element = browser.find_element_by_xpath('//*[@id="tasks"]/div[1]/a[2]')
element.click()
browser.quit()
