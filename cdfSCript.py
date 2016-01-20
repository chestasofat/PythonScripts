__author__ = 'admin'
import collections
import traceback
import sys
import math
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.dates


def read_in_chunks(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


def timeCalculation(timetp, timetp2):
    tm = timetp.split(':')
    hr = tm[0]
    min = tm[1]
    sec = tm[2]
    tm2 = timetp2.split(':')
    hr2 = tm2[0]
    min2 = tm2[1]
    sec2 = tm2[2]
    time1 = (int(hr) * 3600) + int(min) * 60 + int(sec)
    time2 = (int(hr2) * 3600) + int(min2) * 60 + int(sec2)
    diff = (time2 - time1)
    print(diff)
    if (int(diff) < 30):
        return 1
    else:
        return 0


SecWin = []
gyroX = []
gyroY = []
gyroZ = []
rbTag = []
jmTag = []
dataTemp = []
dataTemp2 = []
timetemp = 0
speed = []
tfTag = []
input_file = input("Enter file path :")

try:
    a = open(input_file, 'r')
    i = 1
    for lines in read_in_chunks(a):

        temp = lines.split(',')
        if (timetemp == 0):
            timetemp = temp[0]
        print(timetemp)
        timeDiff = timeCalculation(timetemp, temp[0])
        if (timeDiff == 1):
            SecWin.append(temp[0])
            gyroX.append(temp[1])
            gyroY.append(temp[2])
            gyroZ.append(temp[3])
            rbTag.append(temp[17])
            speed.append(temp[6])
            jmTag.append(temp[18].rstrip('\n'))
            tfTag.append(temp[19].rstrip('\n'))
        else:
            if (('1' in tfTag) ):
                for data in gyroZ:
                    dataTemp.append(data)
                for data2 in speed:
                    dataTemp2.append(data2)
                timetemp = 0
            else:
                timetemp = 0
            i = i + 1
            SecWin.clear()
            gyroX.clear()
            gyroY.clear()
            gyroZ.clear()
            rbTag.clear()
            jmTag.clear()
            speed.clear()
            tfTag.clear()

    print("Total count--->>" + str(len(dataTemp)))
    dataSpeed = np.loadtxt(dataTemp2)
    sorted_data2 = np.sort(dataSpeed)

    dataZ = np.loadtxt(dataTemp)
    sorted_data = np.sort(dataZ)
    yvals = np.arange(len(sorted_data)) / float(len(sorted_data))
    #plt.plot(sorted_data, yvals)
    plt.plot(sorted_data2, yvals)
    plt.savefig("C:\\mtech Data\\congestion\\dataCollection\\3November\\note3\\TrafficLights\\CDF\\speed" + str(i) + '.png')

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
