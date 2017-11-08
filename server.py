#!/usr/bin/python3 
# -*- coding:UTF-8 -*-  
import time 
import os,sys,system
while True:
  time.sleep(5)
  system('sudo python %s.py' %(os.path.dirname(os.path.realpath(__file__)) ))
  time.sleep(55)
