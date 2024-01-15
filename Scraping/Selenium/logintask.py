from selenium import webdriver
import time


def load_driver(url="https://www.google.com"):
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    driver = webdriver.Chrome(options)
    driver.get(url)
    return driver


content = load_driver("http://automated.pythonanywhere.com/login")
print(content.title)
time.sleep(5)
content.close()
