from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\sandeep.kumar01\Desktop\chromedriver-win64\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)  # Selenium 3.x style
driver.get("https://www.google.com")
driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]').send_keys('Selenium')
driver.quit()
