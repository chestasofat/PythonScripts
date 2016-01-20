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
    fileList = glob.glob(input_file + 'earlyMorning.csv')
    c = open("C:\\mtech Data\\congestion\\dataCollection\\diwali data\\nexus\\temp2.csv", 'w')
    print(fileList)
    for file in fileList:
        a = open(file, 'r')
        gyroX = 0
        counter = 0
        timeTemp = 0
        for lines in read_in_chunks(a):

            temp = lines.split(',')

            if ((temp[0] != 'Time elapsed') & (temp[1] != 'x_gy\n')):
                print("Entered!!!")
                if (timeTemp == 0):
                    timeTemp = temp[0]

                if (temp[0] == timeTemp):
                    counter = counter + 1

                    gyroX = gyroX + float(temp[1])

                else:
                    latsum = gyroX / counter

                    print(counter)
                    gyroX = 0
                    counter = 0

                    c.write(str(timeTemp) + ',' + str(latsum) + '\n')
                    timeTemp = temp[0]

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
