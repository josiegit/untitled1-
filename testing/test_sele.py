#coding:utf-8
from time import sleep
from selenium import webdriver
def test_sele():
     driver=webdriver.Chrome()
     driver.get("https://www.baidu.com")
     sleep(10)