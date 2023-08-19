import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # pyautogui.scroll(-35)
    return driver
