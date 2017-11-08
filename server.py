#!/usr/bin/python3 
# -*- coding:UTF-8 -*-  
import time 
import os,sys
while True:
  time.sleep(5)
  os.system('sudo python %s.py' %(os.path.dirname(os.path.realpath(__file__)) ))
  time.sleep(55)
