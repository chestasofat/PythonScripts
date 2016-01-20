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
    fileList = glob.glob(input_file + 'Nexus 5 2.csv')
    c = open(input_file + "\\cleanedFile15Sept.csv", 'w')
    print(fileList)
    for file in fileList:
        a = open(file, 'r')

        accX = 0
        accY = 0
        accZ = 0
        gyroX = 0
        gyroY = 0
        gyroZ = 0
        oriX = 0
        oriY = 0
        oriZ = 0
        magX = 0
        magY = 0
        magZ = 0
        press = 0
        timeTemp = 0
        lat = 0
        lon = 0
        counter = 0
        latCount = 0
        latSpeed = 0
        for lines in read_in_chunks(a):

            temp = lines.split(',')
            checkString = 'id,dated,timed,imei,gen_id,Bus_Route,x_acc,y_acc,z_acc,x_gy,y_gy,z_gy,x_ori,y_ori,z_ori,x_mag,y_mag,z_mag,pressure,GPS_Lat,GPS_Lng,GPS_Speed,GPS_Bearing,GPS_Time,GSM_Lat,GSM_Lng,GSM_Bearing,CId,RSSI,Operator,Bus_Stop,Occupancy,Traffic_Lights,Road_Block,Accidents,event,others,behavior,undone,status'

            #if ((temp[2] != 'timed') & (temp[9] != 'x_gy') & (temp[10] != 'y_gy') & (temp[11] != 'z_gy') & (
                        #temp[19] != 'GPS_Lat') & (temp[20] != 'GPS_Lng') & (temp[21] != 'GPS_Speed')):
            #print(lines)
            #print(checkString)
            if(lines.rstrip('\n') != checkString):
                print("Entered!!!")
                cnt = 0
                while (cnt < 39):
                    if ((temp[cnt] == '') | (temp[cnt] == 'null')):
                        #print(cnt)
                        temp[cnt] = 0
                    cnt = cnt + 1
                if(temp[6] == ''):
                    temp[6] = 0
                if(temp[7] == ''):
                    temp[7] = 0
                if(temp[8] == ''):
                    temp[8] = 0
                if(temp[9] == ''):
                    temp[9] = 0

                if (timeTemp == 0):
                    timeTemp = temp[2]
                if (temp[2] == timeTemp):
                    counter = counter + 1
                    if (counter == 0):
                        latCount = 1
                        counter = 1
                    else:
                        latCount = latCount + 1
                    accX = accX + float(temp[6])
                    accY = accY + float(temp[7])
                    accZ = accZ + float(temp[8])
                    gyroX = gyroX + float(temp[9])
                    gyroY = gyroY + float(temp[10])
                    gyroZ = gyroZ + float(temp[11])
                    oriX = oriX + float(temp[12])
                    oriY = oriY + float(temp[13])
                    oriZ = oriZ + float(temp[14])
                    magX = magX + float(temp[15])
                    magY = magY + float(temp[16])
                    magZ = magZ + float(temp[17])
                    press = press + float(temp[18])
                    lat = lat + float(temp[19])
                    lon = lon + float(temp[20])
                    latSpeed = latSpeed + float(temp[21])
                else:
                    print(temp[2])
                    try:
                        gyroXsum = gyroX / counter
                        gyroYsum = gyroY / counter
                        gyroZsum = gyroZ / counter
                        accXsum = accX / counter
                        accYsum = accY / counter
                        accZsum = accZ / counter
                        oriXsum = oriX / counter
                        oriYsum = oriY / counter
                        oriZsum = oriZ / counter
                        magXsum = magX / counter
                        magYsum = magY / counter
                        magZsum = magZ / counter
                        pressSum = press / counter
                        latgyroSum = lat / latCount
                        longyroSUm = lon / latCount
                        speedGyroSum = latSpeed / latCount
                        #print(timeTemp)
                        #print(lat)
                        #print(latCount)
                        print(counter)
                        gyroX = 0
                        gyroY = 0
                        gyroZ = 0
                        accX = 0
                        accY = 0
                        accZ = 0
                        oriX = 0
                        oriY = 0
                        oriZ = 0
                        magX = 0
                        magY = 0
                        magZ = 0
                        press = 0
                        counter = 0
                        latCount = 0
                        lat = 0
                        lon = 0
                        latSpeed = 0
                        copyString = str(accXsum) + ',' + str(accYsum) + ',' + str(accZsum) + ','
                        copyString2 = str(oriXsum) + ',' + str(oriYsum) + ',' + str(oriZsum) + ',' + str(
                            magXsum) + ',' + str(magYsum) + "," + str(magZsum) + ","
                        c.write(str(timeTemp) + ',' + copyString + str(gyroXsum) + ',' + str(gyroYsum) + ',' + str(
                            gyroZsum) + ',' + copyString2 + str(pressSum) + ',' + str(
                            latgyroSum) + ',' + str(longyroSUm) + ',' + str(speedGyroSum) + '\n')
                    except :
                        print("exception")

                    timeTemp = temp[2]

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
