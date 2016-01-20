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
    fileList = glob.glob(input_file + 'tajRB.csv')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\nexus5\\tajRBConges.csv",'w')
    print(fileList)
    for file in fileList:
        a = open(file , 'r')
        for lines in read_in_chunks(a):
            temp = lines.split(',')
            if((prevLat == 0) & (prevLon == 0)):
                prevLat = float(temp[0])
                prevLon = float(temp[1])
            else:
                dist = haversine(prevLon,prevLat,float(temp[1]),float(temp[0]))
                c.write(str(dist) + ',' + temp[2])
                #prevLat = float(temp[0])
                #prevLon = float(temp[1])
except Exception as e:
    print(e)
