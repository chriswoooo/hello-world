from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
import numpy
import time

# 初始化浏览器
driver = webdriver.Chrome()
print("world")

# 登录
driver.get('https://consumer.huawei.com/cn/phones/')



print(driver)
