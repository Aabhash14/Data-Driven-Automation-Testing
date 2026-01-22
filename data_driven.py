from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import csv, time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

with open(r"C:\Users\ms\Desktop\Selenium\Certificate_Assignment\testdata.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:

        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(row["username"])
        driver.find_element(By.ID, "password").send_keys(row["password"])
        print(f"\nExecuting test with username: {row['username']}")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        if "inventory" in driver.current_url:
            print(f"TEST RESULT: PASS | Login successful for user: {row['username']}")
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(2)
            driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(3)
        else:
            print(f"TEST RESULT: FAIL | Login failed for user: {row['username']}")

print("\n===== DATA-DRIVEN TEST EXECUTION COMPLETED =====")

driver.quit()
