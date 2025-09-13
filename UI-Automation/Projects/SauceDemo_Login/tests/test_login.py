import json
import time

from selenium import webdriver

class Login:
    with open('../data/credentials.json') as f:
        creds = json.load(f)

    username = creds["username"]
    password = creds["password"]

    driver_path = r"C:\Users\sandeep.kumar01\Desktop\chromedriver-win64\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)  # Selenium 3.x style
    driver.get("https://www.saucedemo.com/")
    driver.find_element_by_id('user-name').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    time.sleep(3)

    # 🔹 Verify login success (check URL or element)
    if "inventory" in driver.current_url:
        print("✅ Login Successful!")
    else:
        print("❌ Login Failed!")
    driver.close()
