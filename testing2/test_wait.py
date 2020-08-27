# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class TestWait:
     def setup(self):
          self.driver=webdriver.Chrome()
          self.driver.get("https://ceshiren.com/")
          # self.driver.implicitly_wait(10)
     def test_wait(self):
          self.driver.find_element(By.XPATH,('//*[@class="navigation-topics docked"]')).click()
          def wait(x):
               return len(self.driver.find_element(By.XPATH,'//*[@class="table-heading"]')) >= 1
          WebDriverWait(self.driver,10).until(wait)
          self.driver.find_element(By.XPATH, "//*[@title=\"在最近的一年，一月，一周或一天最活跃的主题\"]").click()