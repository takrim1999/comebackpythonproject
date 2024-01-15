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
response = get_driver("http://automated.pythonanywhere.com/login/")
# time.sleep(2)
response.find_element(
    by="name", value="username").send_keys("automated")
response.find_element(
    by="name", value="password").send_keys("automatedautomated")
response.find_element(
    by="xpath", value="/html/body/div[1]/div/div/div[3]/form/button").click()
# print(element.get_attribute("type"))
time.sleep(5)
response.close()
# print(element.text)
