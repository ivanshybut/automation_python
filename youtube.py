# coding=utf-8
import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('http://youtube.com')
# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('python')
#
# searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# searchButton.click()

time.sleep(5)
driver.close()
driver.quit()
