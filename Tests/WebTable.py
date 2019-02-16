from selenium import webdriver

driver = webdriver.Chrome()
print(driver)
driver.get('C:/Users/VivekShetty/BrowserwithoutExPath/Files/WebTable.html')
elecol = driver.find_elements_by_xpath('//*[@id="emp"]/thead/tr/th')
print(elecol)
print(len(elecol))
elerow = driver.find_element_by_xpath()