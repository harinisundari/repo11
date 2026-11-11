
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_addition():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    try:
        driver.get("http://localhost:8001/calculator.html")

        driver.find_element(By.ID, "num1").send_keys("10")
        driver.find_element(By.ID, "num2").send_keys("20")
        driver.find_element(By.ID, "addBtn").click()

        result = driver.find_element(By.ID, "result").text

        print("Page Title:", driver.title)
        print("Addition Result:", result)

        assert result == "30", "Test Failed: Result mismatch"
        print("Test Completed Successfully")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_addition()
