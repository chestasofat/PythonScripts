__author__ = 'admin'

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
    fileList = glob.glob(input_file + 'dataNewS5.csv')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\s5\\dataCleanWithSpeed.csv", 'w')
    print(fileList)
    for file in fileList:
        a = open(file, 'r')
        gpsLat = 0
        gpgLong = 0
        speed = 0
        timeTemp = 0
        lat = 0
        lon = 0
        counter = 0
        latCount = 0
        latSpeed = 0
        for lines in read_in_chunks(a):

            temp = lines.split(',')

            if ((temp[2] != 'timed') & (temp[9] != 'x_gy') & (temp[10] != 'y_gy') & (temp[11] != 'z_gy') & (
                        temp[19] != 'GPS_Lat') & (temp[20] != 'GPS_Lng') & (temp[21] != 'GPS_Speed')):
                print("Entered!!!")
                if (timeTemp == 0):
                    timeTemp = temp[2]
                if (temp[19] == ""):
                    temp[19] = 0
                if (temp[20] == ""):
                    temp[20] = 0
                if (temp[21] == ""):
                    temp[21] = 0
                if(temp[2] == timeTemp):
                    counter = counter + 1
                    if(counter == 0):
                        latCount = 1
                    else:
                        latCount = latCount + 1
                    gpsLat = gpsLat + float(temp[9])
                    gpgLong = gpgLong + float(temp[10])
                    speed = speed + float(temp[11])
                    lat = lat + float(temp[19])
                    lon = lon + float(temp[20])
                    latSpeed = latSpeed + float(temp[21])
                else:
                    latsum = gpsLat / counter
                    lonsum = gpgLong / counter
                    speedsum = speed / counter
                    latgyroSum = lat / latCount
                    longyroSUm = lon / latCount
                    speedGyroSum = latSpeed /latCount
                    print(timeTemp)
                    print(lat)
                    print(latCount)
                    print(counter)
                    gpsLat = 0
                    gpgLong = 0
                    speed = 0
                    counter = 0
                    latCount = 0
                    lat = 0
                    lon = 0
                    latSpeed = 0
                    c.write(str(timeTemp) + ',' + str(latsum) + ',' + str(lonsum) + ',' + str(speedsum) + ',' + str(
                        latgyroSum) + ',' + str(longyroSUm) + ',' + str(speedGyroSum) +'\n')
                    timeTemp = temp[2]

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
