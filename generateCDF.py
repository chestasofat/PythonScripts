__author__ = 'admin'
import matplotlib.pyplot as plt
import numpy as np
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

legendList = []
input_file = input("Enter file path :")
try:
    fileList = glob.glob(input_file + 'cdfTempEarly.csv')
    for file in fileList:
        data = np.loadtxt(file)
        print(data)
        fileTemp = file.split("\\")
        #filenameTemp = fileTemp[8].split('_')
        filename = fileTemp[6]
        sorted_data = np.sort(data)
        yvals=np.arange(len(sorted_data))/float(len(sorted_data))
        plt.plot(sorted_data,yvals,color = np.random.rand(3,1) )
        legendList.append(filename)
        #sorted_data = []

        x1,x2,y1,y2 = plt.axis()
        plt.legend(legendList,fontsize='xx-small')
        #plt.axis((0,60,y1,y2))
        plt.title("Temporal Speed CDF")
        #plt.setp(legend.get_title(),fontsize='xx-small')
        plt.xlabel('Speed in mps')
        plt.ylabel("Probability")
        plt.savefig("C:\\mtech Data\\congestion\\dataCollection\\surface paper tests\\abc\\" + filename + ".jpg")
        #plt.show()
except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)