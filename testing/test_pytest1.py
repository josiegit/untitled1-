# -*- coding:utf-8 -*-
import pytest
import yaml
from python.calc import Calc

class DataLoad:
     """加载yaml数据"""
     def __init__(self,data_name):
          with open(data_name) as f:
               self.data=yaml.load(f)

     def get_data(self,name):
          return self.data[name]
 
#获取数据
Data1=DataLoad("../data/data_add.yaml")
Data2=DataLoad("../data/data_div.yaml")

#测试类
class Testcalc:
     def setup(self):
          self.calc=Calc()

     #获取正常情况
     @pytest.mark.add
     @pytest.mark.parametrize("a,b,expected", Data1.get_data("norm"))
     def test_add_1(self, a, b, expected):
          result = self.calc.add(a, b)
          assert expected == result
     #获取异常情况
     @pytest.mark.parametrize("a,b,res",Data1.get_data("expect"))
     @pytest.mark.xfail
     def test_add_2(self, a, b, res):
          result = self.calc.add(a, b)

     @pytest.mark.parametrize("data1,data2,data3",[
          (3,3,1),
          (2,2,1)
     ])
     def test_div_1(self, data1, data2, data3):
          try:
               result = self.calc.div(data1, data2)

          except ZeroDivisionError:
               return "division by 0"
               assert result == "division by 0"
          assert data3 == result
if __name__ == "__main__":
     pytest.main('-vs', 'test_pytest.py')
