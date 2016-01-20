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

rbTag = 0
jmTag = 0
tfTag = 0

rboutTimes = []
jmTimes = []
tfLight = []
try:
    rb = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\nexus5\\dataNew.csv",'r')
    for lines in read_in_chunks(rb):
        rbtemp = lines.split(',')
        if(rbtemp[36] == 'RABOUT'):
            rboutTimes.append(rbtemp[2])
        if(rbtemp[36] == 'JAM'):
            jmTimes.append(rbtemp[2])
        if(rbtemp[32] == '1'):
            tfLight.append(rbtemp[2])
    rb.close()

    fileList = glob.glob(input_file + 'dataNewNote3.csv')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\3November\\note3\\TrafficLights\\TLClean.csv", 'w')
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

        x_acc = 0.0
        y_acc = 0.0
        z_acc = 0.0

        x_mag = 0.0
        y_mag = 0.0
        z_mag = 0.0

        x_ori = 0.0
        y_ori = 0.0
        z_ori = 0.0

        press = 0.0

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
                if (temp[6] == ""):
                    temp[6] = 0
                if (temp[7] == ""):
                    temp[7] = 0
                if (temp[8] == ""):
                    temp[8] = 0
                if (temp[12] == ""):
                    temp[12] = 0
                if (temp[13] == ""):
                    temp[13] = 0
                if (temp[14] == ""):
                    temp[14] = 0
                if (temp[15] == ""):
                    temp[15] = 0
                if (temp[16] == ""):
                    temp[16] = 0
                if (temp[17] == ""):
                    temp[17] = 0
                if (temp[18] == ""):
                    temp[18] = 0
                if (temp[2] == timeTemp):
                    counter = counter + 1
                    if (counter == 0):
                        latCount = 1
                    else:
                        latCount = latCount + 1
                    gpsLat = gpsLat + float(temp[9])
                    gpgLong = gpgLong + float(temp[10])
                    speed = speed + float(temp[11])
                    lat = lat + float(temp[19])
                    lon = lon + float(temp[20])
                    latSpeed = latSpeed + float(temp[21])
                    x_acc = x_acc + float(temp[6])
                    y_acc = y_acc + float(temp[7])
                    z_acc = z_acc + float(temp[8])
                    x_ori = x_ori + float(temp[12])
                    y_ori = y_ori + float(temp[13])
                    z_ori = z_ori + float(temp[14])
                    x_mag = x_mag + float(temp[15])
                    y_mag = y_mag + float(temp[16])
                    z_mag = z_mag + float(temp[17])
                    press = press + float(temp[18])

                else:
                    latsum = gpsLat / counter
                    lonsum = gpgLong / counter
                    speedsum = speed / counter
                    latgyroSum = lat / latCount
                    longyroSUm = lon / latCount
                    speedGyroSum = latSpeed / latCount
                    accXSum = x_acc/counter
                    accYSum = y_acc/counter
                    accZSum = z_acc/counter
                    oriXSum = x_ori/counter
                    oriYSum = y_ori/counter
                    oriZSum = z_ori/counter
                    magXSum = x_mag/counter
                    magYSum = y_mag/counter
                    magZSum = z_mag/counter
                    pressSum = press/counter
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
                    x_acc = 0
                    y_acc = 0
                    z_acc = 0

                    x_mag = 0
                    y_mag = 0
                    z_mag = 0

                    x_ori = 0
                    y_ori = 0
                    z_ori = 0

                    press = 0
                    if(temp[2] in rboutTimes):
                        rbTag = 1
                    else:
                        rbTag = 0
                    if(temp[2] in jmTimes):
                        jmTag = 1
                    else:
                        jmTag = 0
                    if(temp[2] in tfLight):
                        tfTag = 1
                    else:
                        tfTag = 0
                    tempString = str(accXSum) + ',' + str(accYSum) + ',' + str(accZSum) + ',' + str(oriXSum) + ',' + str(
                        oriYSum) + ',' + str(oriZSum) + ',' + str(magXSum) + ',' + str(magYSum) + ',' + str(magZSum) + ',' + str(
                        pressSum)
                    c.write(str(timeTemp) + ',' + str(latsum) + ',' + str(lonsum) + ',' + str(speedsum) + ',' + str(
                        latgyroSum) + ',' + str(longyroSUm) + ',' + str(speedGyroSum) + ',' + tempString + ',' + str(rbTag) + ',' + str(jmTag) +',' + str(tfTag)+'\n')
                    tempString = ''
                    timeTemp = temp[2]
                    rbTag = 0
                    jmTag = 0
                    tfTag = 0

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
