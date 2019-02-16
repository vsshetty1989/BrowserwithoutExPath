from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://phptravels.com/')
driver.maximize_window()
driver.delete_all_cookies()
driver.find_element_by_xpath("//span[text()='Login']").click()
current_window_id=driver.current_window_handle
print(current_window_id)
window_ids=driver.window_handles
print(type(window_ids))
for handle in window_ids:
    if handle!=current_window_id:
        driver.switch_to.window(handle)
        driver.find_element_by_name("username").send_keys("test")
driver.close()
#driver.quit()