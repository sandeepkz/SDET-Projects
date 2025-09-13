class ChromeInvoke:
    from selenium import webdriver
    driver_path = r"C:\Users\sandeep.kumar01\Desktop\chromedriver-win64\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)  # Selenium 3.x style

