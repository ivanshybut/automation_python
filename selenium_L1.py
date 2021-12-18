# coding=utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
url = "https://google.com"

try:
    driver.get(url=url)
    time.sleep(5)

    driver.get(url="https://instagram.com")
    time.sleep(5)

    driver.get(url="https://youtube.com")
    time.sleep(3)

finally:
    driver.close()
    driver.quit()


