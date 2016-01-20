__author__ = 'admin'
import collections
import traceback
import sys
import math
import numpy as np


filePath = input("Enter file path:")
kthVal = input("Enter the kth value")
speeds = []

def read_in_chunks(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

a = open(filePath,'r')
for lines in read_in_chunks(a):
        temp = lines.split(',')
        if((temp[2] != 'GPS_Speed') & (temp[2] != '')):
            speeds.append(float(temp[2]))
speedTemp = []
speeds.sort()
#print(speeds)
index = (int(len(speeds))*(int(kthVal)/100))
print(index)
print(str(speeds[int(index-1)]))
#print(len(speeds))
