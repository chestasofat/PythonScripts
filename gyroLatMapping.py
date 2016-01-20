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


input_file = input("Enter file path :")
#pressureArray = collections.deque(maxlen=15)
pressureArray = []
lats = []
#print(sys.argv[1:])
pressureFlag = 0
try:
    a = open(input_file, 'r')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\note3\\maps\\onlyGyro30sec.csv", 'w')
    i = 0
    for lines in read_in_chunks(a):
        temp = lines.split(',')
        #print(temp[3])
        pressureArray.append(float(temp[3]))
        lats.append(temp[0] + ','+ temp[4] + ',' + temp[5] + ',' + temp[6])
        pressureArray.sort()
        i = i + 1
        if (i == 30):
            print('new window--->>')
            var1 = 0
            var2 = 0
            '''while (pressureArray):
                var1Temp = float(pressureArray.pop())
                if(var1>var1Temp):
                    var1 = var1Temp
                var2Temp = float(pressureArray.pop())
                if(var2<var2Temp):
                    var2 = var2Temp'''
            var1 = pressureArray[0]
            var2 = pressureArray[29]
            diff = (float(var2) - float(var1))
            print('Difference------>>>' + str(diff))
            #if( (diff < -0.05000) | (diff > 0.05000) & (0.0000 <float(temp[6]) < 8.000)):
            if( (diff > 0.05000) | (diff < -0.05000) ):
                print('<<<------------Winner Difference------->>>>>' )
                for data in lats:
                    c.write(data)
            i = 0
            pressureArray.clear()
            lats.clear()


except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
