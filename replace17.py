__author__ = 'admin'
import matplotlib.pyplot as plt
import numpy as np
import glob
import traceback
import sys


def read_in_chunks(file_object):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


input_file = input("Enter file path :")
i = 1
j = 0
timeTT = 0
try:
    fileList = glob.glob(input_file + 'data.csv')
    c = open("C:\\mtech Data\\congestion\\roundAbouts\\dataClean.csv", 'w')
    print(fileList)
    for file in fileList:
        a = open(file, 'r')
        gpsLat = 0
        gpgLong = 0
        speed = 0
        timeTemp = 0
        lat = 0
        lon = 0
        for lines in read_in_chunks(a):

            temp = lines.split(',')
            if (timeTemp == 0):
                timeTemp = temp[2]
            if ((temp[2] != 'timed') & (temp[9] != 'x_gy') & (temp[10] != 'y_gy') & (temp[11] != 'z_gy') & (
                        temp[19] != 'GPS_Lat') & (temp[20] != 'GPS_Lng')):
                if (temp[19] == ""):
                    temp[19] = 0
                if (temp[20] == ""):
                    temp[20] = 0
                # timeTemp = temp[2]
                if (timeTemp == temp[2]):
                    gpsLat = gpsLat + float(temp[9])
                    gpgLong = gpgLong + float(temp[10])
                    speed = speed + float(temp[11])
                    lat = lat + float(temp[19])
                    lon = lon + float(temp[20])
                    # if (i % 17 == 0):
                    #i = 1

                latsum = gpsLat / 17
                lonsum = gpgLong / 17
                speedsum = speed / 17
                latgyroSum = lat / 17
                longyroSUm = lon / 17
                    # print(gpsLat)

                    # print(latsum)
                gpsLat = 0
                gpgLong = 0
                speed = 0
                c.write(str(timeTemp) + ',' + str(latsum) + ',' + str(lonsum) + ',' + str(speedsum) + ',' + str(
                    latgyroSum) + ',' + str(longyroSUm) + '\n')
                    # c.write(str(timeTemp))
                #i = i + 1
                timeTemp = temp[2]
except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
