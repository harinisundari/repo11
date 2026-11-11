
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get("http://localhost:8001/registration.html")
    yield driver
    driver.quit()


def register(driver, username, email, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "registerBtn").click()

    return driver.find_element(By.ID, "message").text


def test_username_empty(setup_teardown):
    message = register(
        setup_teardown, "", "user@example.com", "Strong@123"
    )
    assert message == "Username is required"
    print("Empty username test PASSED")


def test_invalid_email(setup_teardown):
    message = register(
        setup_teardown, "harini", "invalid-email", "Strong@123"
    )
    assert message == "Enter a valid email address"
    print("Invalid email test PASSED")


def test_weak_password(setup_teardown):
    message = register(
        setup_teardown, "harini", "user@example.com", "weak"
    )
    assert message.startswith("Password must have")
    print("Weak password test PASSED")


def test_valid_registration(setup_teardown):
    message = register(
        setup_teardown, "harini", "user@example.com", "Strong@123"
    )
    assert message == "Registration successful!"
    print("Valid registration test PASSED")
