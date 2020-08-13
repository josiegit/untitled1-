# -*- coding:utf-8 -*-

import pytest
from python.calc import Calc
import yaml

class TestCalc:
     @pytest.mark.parametrize("a,b,expected",yaml.load(open("../data_add.yaml")))
     def test_add_1(self,a,b,expected):
          self.calc = Calc()
          result = self.calc.add(a,b)
          assert expected  == result
     @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open(./"data_div.yaml")))
     def test_div_1(self,a,b,expected):
          self.calc=Calc()
          result=self.calc.div(a,b)
          assert expected == result



if __name__=="__main__":
     pytest.main('-vs','test_pytest.py')