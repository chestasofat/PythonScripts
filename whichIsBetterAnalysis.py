__author__ = 'admin'
import collections
import traceback
import sys
from math import radians, cos, sin, asin, sqrt
import math
import numpy as np
import requests

def haversine(lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def read_in_chunks(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def calculateTime(timeT):
    tmp = timeT.split(':')
    hh = float(tmp[0])*3600
    min = float(tmp[1])*60
    sec = float(tmp[2])
    timeRes = hh + min + sec
    return int(timeRes)

input_file = input("Enter file path :")
refernceFile = input("Enter file path(reference) :")
RbLatLon = []
fileForTags = ''
try:
    fileForTags = open(refernceFile, 'r')
    for lines in read_in_chunks(fileForTags):
        checkString = 'id,dated,timed,imei,gen_id,Bus_Route,x_acc,y_acc,z_acc,x_gy,y_gy,z_gy,x_ori,y_ori,z_ori,x_mag,y_mag,z_mag,pressure,GPS_Lat,GPS_Lng,GPS_Speed,GPS_Bearing,GPS_Time,GSM_Lat,GSM_Lng,GSM_Bearing,CId,RSSI,Operator,Bus_Stop,Occupancy,Traffic_Lights,Road_Block,Accidents,event,others,behavior,undone,status'
        if(lines.rstrip('\n') != checkString):
            temp = lines.split(',')
            if((temp[19] == '') | (temp[19] == 'null')):
                temp[19] = 0
            if((temp[20] == '') | (temp[20] == 'null')):
                temp[20] = 0
            if(int(temp[32]) == 1 ):
                RbLatLon.append(str(temp[19]) + ':' + str(temp[20]) )
    print(RbLatLon)
except Exception as e:
    print(e)
    print("Error in reading first file")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
fileForTags.close()
timeTemp = 0
timeCal = []
latLonTemp = []
try:
    a = open(input_file, 'r')
    c = open(input_file + 'TrafficbetterSmall RadiusAnalysis.csv','w')

    for lines in read_in_chunks(a):

        checkString = 'id,dated,timed,imei,gen_id,Bus_Route,x_acc,y_acc,z_acc,x_gy,y_gy,z_gy,x_ori,y_ori,z_ori,x_mag,y_mag,z_mag,pressure,GPS_Lat,GPS_Lng,GPS_Speed,GPS_Bearing,GPS_Time,GSM_Lat,GSM_Lng,GSM_Bearing,CId,RSSI,Operator,Bus_Stop,Occupancy,Traffic_Lights,Road_Block,Accidents,event,others,behavior,undone,status'
        if(lines.rstrip('\n') != checkString):
            temp = lines.split(',')

            cnt = 0
            while (cnt < 39):
                if ((temp[cnt] == '') | (temp[cnt] == 'null')):
                    temp[cnt] = 0
                cnt = cnt + 1


            difference = 0
            if(timeTemp == 0):
                timeTemp = temp[2]
            currentTime = calculateTime(temp[2])
            prevTime = calculateTime(timeTemp)
            if (int(currentTime) < (int(prevTime) + 300)):
                #print(prevTime)
                #print("In if part------->>>>")
                latCheck = float(temp[19])
                lonCheck = float(temp[20])
                for data in RbLatLon:
                    geolt = data.split(":")
                    lt = float(geolt[0])
                    lon = float(geolt[1])
                    distance = haversine(lon,lt,lonCheck,latCheck)
                    #print(distance)
                    latTemp = 0
                    counter = 0
                    if( float(distance) < 0.0250):
                        #print(latCheck,lonCheck)
                        #print("Check distance------->>>>")
                        latTemp = latTemp + lt
                        counter = counter + 1
                        timeCal.append(currentTime)
                        latLonTemp.append(str(latTemp/counter))
                        #print(currentTime)
                        #print(temp[2])

            else:
                #print("In else part------->>>>")
                if(timeCal != []):
                    #print(timeCal)
                    difference = float(timeCal[len(timeCal) - 1]) - float(timeCal[0])
                    c.write(str(difference) + '\n')
                    #print(latLonTemp)
                timeCal.clear()
                latLonTemp.clear()
                #print(difference)

                timeTemp = temp[2]


    a.close()
    RbLatLon.clear()
except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
