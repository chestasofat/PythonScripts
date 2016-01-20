__author__ = 'chesta'

import sys, traceback
import matplotlib.pyplot as plt
import numpy as np

def read_in_chunks(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

rbSpeed = []
jamSpeed = []
strSpeed = []
legendList = []
try:
    a = open("C:\\Users\\admin\\Desktop\\cdfPlot.csv", 'r')
    for lines in read_in_chunks(a):
        temp = lines.split(',')
        if(temp[1] != ' ') :
            temp[1] = 0.0
        if(temp[2] != ' ') :
            print(temp[2])
            temp[2] = 0.0
        if(temp[3] != ' ') :
            temp[3] = 0.0
        rbSpeed.append(float(temp[1])*3.6)
        rbSpeed.append(float(temp[2])*3.6)
        rbSpeed.append(float(temp[3])*3.6)
    data = np.loadtxt(rbSpeed)
    sorted_data = np.sort(data)
    legendList.append('Round About')
    yvals = np.arange(len(sorted_data)) / float(len(sorted_data))
    plt.plot(sorted_data, yvals)

    data2 = np.loadtxt(jamSpeed)
    sorted_data2 = np.sort(data2)
    legendList.append('JAM')
    yvals2 = np.arange(len(sorted_data2)) / float(len(sorted_data2))
    plt.plot(sorted_data2, yvals2)

    data3 = np.loadtxt(strSpeed)
    sorted_data3 = np.sort(data3)
    legendList.append('Straight Road')
    yvals3 = np.arange(len(sorted_data3)) / float(len(sorted_data3))
    plt.plot(sorted_data3, yvals3)


    plt.legend(legendList,fontsize='xx-small')
    plt.title("Speed CDF")
    plt.xlabel('Speed in KMPH')
    plt.ylabel("Probability")
    plt.show()

except Exception as e:
    print("Exception in ploting!!!!")
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
