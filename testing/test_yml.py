# -+- coding:utf-8 -*-
import yaml

with open('test.yml') as f:
     print(yaml.safe_load(f))