__author__ = 'admin'
import collections
import traceback
import sys
import math
import numpy as np
import requests


def read_in_chunks(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

times = []
input_file = input("Enter file path :")
try:
    a = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\nexus5\\dataNew.csv", 'r')
    for lines in read_in_chunks(a):
        temp = lines.split(',')
        if(temp[37] == 'RABOUT'):
            times.append(temp[2])
    a.close()
    b = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\note3\\maps\\dataNew.csv", 'r')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\note3\\maps\\TimeAnalysisAllSensorsWithoutSpeed15SecNew.csv", 'w')
    #for()
except Exception as e:
    print(e)