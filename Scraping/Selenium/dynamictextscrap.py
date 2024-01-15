from selenium import webdriver
import time


def get_driver(url="https://www.google.com"):
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("disable-infobars")
    # options.add_argument("start-maximized")
    options.add_argument("disable-blink-features-AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-dev-shm-usage")
    driver = webdriver.Chrome(options)
    driver.get(url)
    return driver


# "http://automated.pythonanywhere.com"
response = get_driver("http://automated.pythonanywhere.com")
time.sleep(2)
element = response.find_element(
    by="xpath", value="/html/body/div[1]/div/h1[2]")

print(element.text)
print(element.text.split(": ")[1])
