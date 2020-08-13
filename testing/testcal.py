# -*- coding:utf-8 -*-
import unittest

from python.calc import Calc

class TestCal(unittest.TestCase):
     def test_add_1(self):
          self.calc=Calc()
          result=self.calc.add(1,3)
          self.assertEqual(4,result)
          print(result)