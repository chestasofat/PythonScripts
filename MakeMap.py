__author__ = 'Ashutosh Raina'


import sys, traceback
import glob



def read_in_chunks(file_object):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def makemap(data,filen):
    ge = open('C:\\mtech Data\\congestion\\dataCollection\\3November\\s5\\maps\\googleMaps\\'+filen+'.html', 'w')  # path the create the map file
    cnt = len(data)
    ge.write('<!DOCTYPE html>')
    ge.write('<html>')
    ge.write('  <head>')
    ge.write('    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">')
    ge.write('    <meta charset="utf-8">')
    ge.write('    <title>Simple Polylines</title>')
    ge.write('    <style>')
    ge.write('      html, body, #map-canvas {')
    ge.write('        height: 100%;')
    ge.write('        margin: 0px;')
    ge.write('        padding: 0px')
    ge.write('      }')
    ge.write('    </style>')
    ge.write('    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true"></script>')
    ge.write('    <script>')
    ge.write('function initialize() {')
    ge.write('  var mapOptions = {')
    ge.write('    zoom: 10,')
    ge.write('    center: new google.maps.LatLng(30.76597029,76.78307852),')
    ge.write('    mapTypeId: google.maps.MapTypeId.TERRAIN')
    ge.write('  };')
    ge.write('')
    ge.write('  var map = new google.maps.Map(document.getElementById(\'map-canvas\'),')
    ge.write('      mapOptions);')
    ge.write('')
    ge.write('  var flightPlanCoordinates = [')
    print(cnt)
    for i in range(0,cnt-1):
        #print(i)
        #print(data[i])
        try:
            ge.write('new google.maps.LatLng(' + str(data[i][0]) + ',' + str(data[i][1]) + '),')
        except:
            print("Skipped!!!!!")
            continue
    ge.write('  ];')
    ge.write('for (var i = 0; i < flightPlanCoordinates.length-1; i++) {')
    ge.write('  var marker = new google.maps.Marker({')
    ge.write('      position: flightPlanCoordinates[i],')
    ge.write('      map: map,')
    ge.write('  });')
    ge.write('  }')
    ge.write('  var speed = [')
    for sp in range(0, cnt-1):
        try:
            ge.write(str(data[sp][2]) + ',')
        except:
            continue
    ge.write('];')
    ge.write('  for (var i = 0; i < flightPlanCoordinates.length-1; i++) {')
    ge.write('    if(speed[i]>=0 && speed[i]<=5){')
    ge.write('      var PathStyle = new google.maps.Polyline({')
    ge.write('        path: [flightPlanCoordinates[i], flightPlanCoordinates[i+1]],')
    ge.write("        strokeColor: '#FF0000',")
    ge.write('        strokeOpacity: 0.0,')
    ge.write('        strokeWeight: 8,')
    ge.write('        map: map')
    ge.write('      });')
    ge.write('      }')

    ge.write('    }')
    ge.write('  flightPath.setMap(map);')
    ge.write('}')
    ge.write('google.maps.event.addDomListener(window, \'load\', initialize);')
    ge.write('')
    ge.write('    </script>')
    ge.write('  </head>')
    ge.write('  <body>')
    ge.write('    <div id="map-canvas"></div>')
    ge.write('  </body>')
    ge.write('</html>')
    ge.close()




filePath = input("Enter Path :")
#a = open("C:\\IITB\\Readings\\6thJulyTrip\\Car Taxi CabJul 6, 2015 5_15_27 PMLog.csv",'r')

fileList = glob.glob(filePath + '*.csv')
try:
    for file in fileList:
        arr = [[],[],[]]
        a = open(file, 'r')
        fileTemp = file.split("\\")
        filename = fileTemp[7]
        print(filename)
        i = 0
        for line in read_in_chunks(a):
            temp = line.split(',')
            arr.append([])
            if temp[0] != 'null':
                arr[i].append(temp[0])
                arr[i].append(temp[1])
                arr[i].append(float(temp[2])*3.6)
                #arr[i].append(temp[5])
                i = i + 1
            #print(arr)
        makemap(arr,filename)
except Exception as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
