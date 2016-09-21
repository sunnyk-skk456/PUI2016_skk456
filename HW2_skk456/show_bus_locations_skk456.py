# Author: Sunny Kulkarni (skk456), NYU, September 20
##############################
# Code written to demonstrate ho to pass arguments to a python script
# for HW2
##############################
# put your name as input argument:
# i.e. run the code as
#      python aSimplePythonScript.py Dr.Bianco
# notice that your name should be

# the next line import packages that change the python 2 print function       
# so that it require the same syntax as python 3                               
# thus the code will work both in python 2 and python 3                        
from __future__ import print_function
# the next import allows me to read line input arguments                       
import sys
import csv
import requests
import json
import numpy as np
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


#def get_jsonparsed_data(url):

# this line checks how many arguments are passed to python
# the arguments are stored in sys.argv which is a list
# the first argument is the name of the code
# so sys.argv is a list with at least one element
# with your name in input it will be a list of 2
# if you add more than one word as argument it will give you an error as well

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_skk456.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# this line prints Hallo and then your name
# which you provide as argument

v_mtaurl = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

jsonurl = urllib.urlopen(v_mtaurl)

v_data = jsonurl.read().decode("utf-8")
v_text = json.loads(v_data)

v_buses = v_text['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

v_busno = np.size(v_text['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print("Bus Line : " + sys.argv[2])
print("Number of Active Buses : %d" %(v_busno))

for i in range(v_busno):
    v_lat = v_buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    v_lon = v_buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus %d is at latitude %f and longitude %s" %(i,v_lat,v_lon))
