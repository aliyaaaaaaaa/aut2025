from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://example.com")
print(driver.title)
driver.quit()
