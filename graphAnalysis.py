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

def timeCalculation(timetp,timetp2):
    tm = timetp.split(':')
    hr = tm[0]
    min = tm[1]
    sec = tm[2]
    tm2 = timetp2.split(':')
    hr2 = tm2[0]
    min2 = tm2[1]
    sec2 = tm2[2]
    time1 = (int(hr)*3600) + int(min)*60 + int(sec)
    time2 = (int(hr2)*3600) + int(min2)*60 + int(sec2)
    diff = (time2 - time1)
    print(diff)
    if(int(diff) < 30):
        return 1
    else:
        return 0

SecWin = []
gyroX = []
gyroY = []
gyroZ = []
rbTag = []
jmTag = []
tfTag = []
dataTemp = []
timetemp = 0
input_file = input("Enter file path :")

try:
    a = open(input_file, 'r')
    i = 1
    for lines in read_in_chunks(a):

        temp = lines.split(',')
        if(timetemp == 0):
            timetemp = temp[0]
        print(timetemp)
        timeDiff = timeCalculation(timetemp,temp[0])
        if(timeDiff == 1):
            SecWin.append(temp[0])
            gyroX.append(temp[1])
            gyroY.append(temp[2])
            gyroZ.append(temp[3])
            rbTag.append(temp[17])
            tfTag.append(temp[19].rstrip('\n'))
            jmTag.append(temp[18].rstrip('\n'))
        else:
            if( ('1' in tfTag) ):
                #dates = plt.dates.date2num(SecWin)
                #plt.plot_date(SecWin, gyroX)
                secTemp = []
                j = 0
                for data in SecWin:
                    secTemp.append(j)
                    j=j+1

                plt.plot(secTemp,gyroZ)
                plt.savefig("C:\\mtech Data\\congestion\\dataCollection\\3November\\note3\\TrafficLights\\" + str(i) + '.png')
                plt.close()
                timetemp = 0
            else:
                timetemp = 0
            i = i+1
            SecWin.clear()
            gyroX.clear()
            gyroY.clear()
            gyroZ.clear()
            rbTag.clear()
            jmTag.clear()
            tfTag.clear()

except Exception as e:
    print(e)
