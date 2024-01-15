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
response = get_driver("http://instagram.com")
time.sleep(3)
username = response.find_element(
    by="name", value="username")
username.send_keys("takrim1999")
password = response.find_element(
    by="name", value="password")
password.send_keys("NDC11811051")
loginbutton = response.find_element(
    by="xpath", value="//*[@id=\"loginForm\"]/div/div[3]/button/div")
# print(loginbutton.get_attribute(""))
loginbutton.click()
time.sleep(5)
notsave = response.find_element(
    by="xpath", value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
notsave.click()
time.sleep(15)
response.close()
# print(element.text)
