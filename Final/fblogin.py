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
response = get_driver("http://facebook.com")
# time.sleep(2)
response.find_element(
    by="id", value="email").send_keys("01315343065")
response.find_element(
    by="id", value="pass").send_keys("krim123")
time.sleep(5)
response.find_element(
    by="name", value="login").click()
# response.find_element(
#     by="xpath", value="/html/body/div[1]/div/div/div[3]/form/button").click()
# print(element.get_attribute("type"))
time.sleep(5)
print(response.find_element(by="xpath",value="//*[@id=\"mount_0_0_pC\"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span"))
response.close()
# print(element.text)
