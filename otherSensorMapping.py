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
# pressureArray = collections.deque(maxlen=15)
pressureArray = []
oriArray = []
magXArray = []
magYArray = []
lats = []
# print(sys.argv[1:])
pressureFlag = 0
try:
    a = open(input_file, 'r')
    c = open(
        "C:\\mtech Data\\congestion\\dataCollection\\diwali data\\nexus\\resultMag.csv",
        'w')
    i = 0
    for lines in read_in_chunks(a):
        temp = lines.split(',')
        # print(temp[3])
        pressureArray.append(float(temp[3]))
        oriArray.append(float(temp[10]))
        magXArray.append(float(temp[13]))
        magYArray.append(float(temp[14]))
        lats.append(
            temp[0] + ',' + temp[4] + ',' + temp[5] + ',' + temp[6] + ',' + temp[7] + ',' + temp[8] + ',' + temp[
                9] + ',' + temp[10] + ',' + temp[11] + ',' + temp[12] + ',' + temp[13] + ',' + temp[14] + ',' + temp[
                15] + ',' + temp[16])
        pressureArray.sort()
        oriArray.sort()
        magXArray.sort()
        magYArray.sort()
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
            oriMax = oriArray[29]
            oriMin = oriArray[0]
            oriDiff = (float(oriMax) - float(oriMin))
            print('Difference Ori------>>>' + str(oriDiff))

            magXMax = magXArray[29]
            magXMin = magXArray[0]
            magXDiff = (float(magXMax) - float(magXMin))
            print('Difference MagX------>>>' + str(magXDiff))

            magYMax = magYArray[29]
            magYMin = magYArray[0]
            magYDiff = (float(magYMax) - float(magYMin))
            #stdev = np.std(magXArray)

            stddev = 0
            average = 0
            average = np.mean(magYArray) #or calculate it yourself
            diffsquared = 0
            sum_diffsquared = 0
            for val in magYArray:
              diffsquared = (val-average)**2
              sum_diffsquared = diffsquared + sum_diffsquared
            stddev = ((sum_diffsquared)/len(magYArray)**(1/2))



            print('Difference MagY------>>>' + str(magYDiff))
            print('STD------>>>' + str(stddev))

            # if( (diff < -0.05000) | (diff > 0.05000) & (0.0000 <float(temp[6]) < 8.000)):
            '''if (((diff > 0.05000) | (diff > 0.05000)) & (300.0 > oriDiff > 60.0) & ((magXDiff > 10.0)&(magYDiff > 10.0))):
                print('<<<------------Winner Difference------->>>>>')
                for data in lats:
                    c.write(data)'''

            if (stddev > 2.00):
                print('<<<------------Not congested------->>>>>')
                for data in lats:
                    c.write(data)
            i = 0
            pressureArray.clear()
            oriArray.clear()
            lats.clear()
            magXArray.clear()
            magYArray.clear()


except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
