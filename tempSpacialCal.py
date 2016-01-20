__author__ = 'admin'
import matplotlib.pyplot as plt
import numpy as np
import glob
import traceback
import sys
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
def read_in_chunks(file_object):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

input_file = input("Enter file path :")
timeTemp = 0
prevLat = 0
prevLon = 0
try:
    fileList = glob.glob(input_file + 'cleanedFile2.csv')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\surface paper tests\\em2\\DifferenceFile.csv",'w')
    print(fileList)
    for file in fileList:
        a = open(file , 'r')
        for lines in read_in_chunks(a):
            temp = lines.split(',')
            tm = temp[0].split(':')
            hr = int(tm[0])
            min = int(tm[1])
            sec = int(tm[2])

            if(timeTemp == 0):
                timeTemp = hr + min/60 + sec/3600
            if(prevLat == 0):
                prevLat = temp[1]
            if(prevLon == 0):
                prevLon = temp[2]

            latDiff = haversine(float(prevLon),float(prevLat),float(temp[2]),float(temp[1]))
            timeDiff = (hr + min/60 + sec/3600) - int(timeTemp)
            timeDiff = timeDiff*3600
            c.write(str(timeDiff) + ',' + str(latDiff*1000)  + ',' + str(temp[3]) )
            #prevLat = temp[1]
            #prevLon = temp[2]
            #timeTemp = hr + min/60 + sec/3600

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
