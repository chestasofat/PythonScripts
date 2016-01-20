__author__ = 'admin'
import collections
import traceback
import sys
import math
import numpy
import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


def read_in_chunks(file_object):
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


input_file = input("Enter file path :")
#referFile = input("Enter reference file path :")
# pressureArray = collections.deque(maxlen=15)
referArrayAccX = []
referArrayMagX = []
accXArray = []
latarray = []
lonArray = []

try:
    refer = open('C:\\mtech Data\\congestion\\analysis\\pearsonCoeff\\referenceFile.csv','r')
    a = open(input_file, 'r')
    c = open('C:\\mtech Data\\congestion\\analysis\\pearsonCoeff\\' +
             "result.csv",
             'w')
    i = 0
    for lines in read_in_chunks(refer):
        temps = lines.split(',')
        referArrayAccX.append(float(temps[0]))
    for lines in read_in_chunks(a):
        checkString = 'id,dated,timed,imei,gen_id,Bus_Route,x_acc,y_acc,z_acc,x_gy,y_gy,z_gy,x_ori,y_ori,z_ori,x_mag,y_mag,z_mag,pressure,GPS_Lat,GPS_Lng,GPS_Speed,GPS_Bearing,GPS_Time,GSM_Lat,GSM_Lng,GSM_Bearing,CId,RSSI,Operator,Bus_Stop,Occupancy,Traffic_Lights,Road_Block,Accidents,event,others,behavior,undone,status'
        if(lines.rstrip('\n') != checkString):
            temp = lines.split(',')
            accXArray.append(float(temp[8]))
            latarray.append(temp[19] + ',' + temp[20] )
            lonArray.append((temp[20]))
            i = i + 1
            res = 0
            if (i == 684):
                res = pearson_def(accXArray, referArrayAccX)
                print("Pearson Coeff--------->>" + str(res))
                if( (res > 0.0) & (res <0.19)):
                    for val in latarray:
                        c.write(val + ',' +'very weak' + '\n')
                if( (res > 0.60) & (res <0.79)):
                    for val in latarray:
                        c.write(val + ',' +'strong' + '\n')
                if( (res > 0.80) & (res <1.0)):
                    for val in latarray:
                        c.write(val + ',' +'very strong' + '\n')
                i = 0
                accXArray.clear()
                latarray.clear()
                lonArray.clear()

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
