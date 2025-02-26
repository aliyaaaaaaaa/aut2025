from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost")
print(driver.title)
driver.quit()
