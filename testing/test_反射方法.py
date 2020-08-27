# -*- coding:utf-8 -*-
class Person:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name} is eating')
p=Person("jerry")
print(p.eat())
print(hasattr(p,"haha"))#判断实例有没有属性或方法
f=getattr(p,"eat")
f()
print(getattr(p,"haha","hou"))
