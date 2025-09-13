from selenium import webdriver

class ChromeInvoke:
    def __init__(self):
        driver_path = r"C:\Users\sandeep.kumar01\Desktop\chromedriver-win64\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)  # Selenium 3.x style
