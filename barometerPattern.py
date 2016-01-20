__author__ = 'admin'

import matplotlib.pyplot as plt
import numpy as np
import glob
import traceback
import sys
import collections
from collections import deque
from itertools import islice
import math


def sliding_window(iterable, size=25, step=1, fillvalue=None):
    print("Inside Function------------->>>")
    if size < 0 or step < 1:
        raise ValueError
    it = iter(iterable)
    q = deque(islice(it, size), maxlen=size)
    print(q)
    if not q:
        return  # empty iterable or size == 0
    q.extend(fillvalue for _ in range(size - len(q)))  # pad to size
    while True:
        yield iter(q)  # iter() to avoid accidental outside modifications
        q.append(next(it))
        q.extend(next(it, fillvalue) for _ in range(step - 1))


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
try:
    fileList = glob.glob(input_file + '*.csv')
    c = open("C:\\mtech Data\\congestion\\test script\\cleanedFile.csv", 'w')
    print(fileList)
    for file in fileList:
        a = open(file, 'r')
        line = ''
        dq = collections.deque(maxlen=2040)
        dqTemp = collections.deque(maxlen=2040)
        i = 0
        diffFlag = 0
        for lines in read_in_chunks(a):
            # line = sliding_window(lines)
            # print(line)
            # for _ in range(2050):
            dq.append(lines)
            dqTemp.append(lines)
            i = i + 1
            # repeated compute

            if (i == 2040):
                diffFlag = 0
                dq.reverse()
                dqTemp.reverse()
                try:
                    while (dq):
                        # print(dq)
                        tempLine1 = dq.pop()
                        #print(tempLine1)
                        tmp1 = tempLine1.split(',')
                        tempLine2 = dq.pop()
                        tmp2 = tempLine2.split(',')
                        diff = 0
                        #print(tmp1[18])
                        if ((tmp1[18] != 'pressure') & (tmp1[18] != '') & (tmp2[18] != '')):
                            diff = math.fabs(float(tmp2[18]) - float(tmp1[18]))
                            #print(diff)
                        if (float(diff) > 0.1000):
                            diffFlag = 1
                            break
                    while (dqTemp):
                        tp = dqTemp.pop()
                        strTemp = tp.rstrip('\n') + ',' + str(diffFlag) + ',' + '\n'
                        # print(diffFlag)
                        c.write(strTemp)
                        strTemp = ''
                    diffFlag = 0
                    dq.clear()
                    dqTemp.clear()
                    i = 0

                except StopIteration as e:
                    print(e)

except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
