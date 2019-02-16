from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
print(driver)
driver.get('https://flipkart.com')
driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
driver.maximize_window()
driver.implicitly_wait(10)
element_to_hover = driver.find_element_by_xpath("//span[text()='Men']")
hover = ActionChains(driver).move_to_element(element_to_hover)
hover.perform()

