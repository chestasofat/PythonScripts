__author__ = 'admin'
import collections
import traceback
import sys
import math


def read_in_chunks(file_object):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


input_file = input("Enter file path :")
input_tag = input("Enter the tag:")
pressureArray = collections.deque(maxlen=2040)
pressureFlag = 0
try:
    a = open(input_file, 'r')
    c = open(input_file + "out.csv", 'w')
    i = 0
    for lines in read_in_chunks(a):
        checkString = 'id,dated,timed,imei,gen_id,Bus_Route,x_acc,y_acc,z_acc,x_gy,y_gy,z_gy,x_ori,y_ori,z_ori,x_mag,y_mag,z_mag,pressure,GPS_Lat,GPS_Lng,GPS_Speed,GPS_Bearing,GPS_Time,GSM_Lat,GSM_Lng,GSM_Bearing,CId,RSSI,Operator,Bus_Stop,Occupancy,Traffic_Lights,Road_Block,Accidents,event,others,behavior,undone,status'
        if(lines.rstrip('\n') != checkString):
            temp = lines.split(',')
            pressureArray.append(temp[2] + ',' +temp[11]+ ',' + temp[21])
            i = i + 1
            if input_tag in lines:
                pressureFlag = 1
            if (pressureFlag == 1) & (i == 100):
                pressureArray.reverse()
                print("Enter---->>>")
                #c.write("New Window--->>" + '\n')
                while (pressureArray):
                    #var1 = pressureArray.pop()
                    #var1 = var1.split(',')
                    #var1a = float(var1[1])
                    var2 = pressureArray.pop()
                    var2 = var2.split(',')
                    #var2a = float(var2[1])
                    #diff = math.fabs(var2a - var1a)
                    c.write(str(var2[0])+ ',' + str(var2[1]) + ',' + str(var2[2]) +',RABOUT' + '\n')
                i = 0
                pressureFlag = 0
                pressureArray.clear()
            if (i == 100) & (pressureFlag == 0):
                i = 0

                while (pressureArray):
                    #var1 = pressureArray.pop()
                    #var1 = var1.split(',')
                    #var1a = float(var1[1])
                    var2 = pressureArray.pop()
                    var2 = var2.split(',')
                    #var2a = float(var2[1])
                    #diff = math.fabs(var2a - var1a)
                    c.write(str(var2[0])+ ',' + str(var2[1]) + ',' + str(var2[2]) +',NORMAL' + '\n')


                pressureArray.clear()
                pressureFlag = 0
            if (i != 100):
                continue
except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
