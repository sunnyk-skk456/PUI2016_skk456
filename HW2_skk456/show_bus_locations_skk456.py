# Author: Sunny Kulkarni (skk456), NYU, September 20
##############################
# Code written to pull data from MTA website and display Bus Name, Active Buses and their latitude and longitude positions.
##############################
                        
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


# To run this code - 
#    python show_bus_locations_skk456.py <MTA_KEY> <BUS_LINE>

# If 2 arguments are not found, code gives error and describes the issue.

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_skk456.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# Store the MTA URL in variable v_mtaurl

v_mtaurl = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

jsonurl = urllib.urlopen(v_mtaurl)

# The data from the URL is stored in variable v_text
v_data = jsonurl.read().decode("utf-8")
v_text = json.loads(v_data)

# Get the list in variable v_buses
v_buses = v_text['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# Get the number of buses in variable v_busno
v_busno = np.size(v_text['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print("Bus Line : " + sys.argv[2])
print("Number of Active Buses : %d" %(v_busno))

for i in range(v_busno):
    # Store latitude information in variable v_lat
    v_lat = v_buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    # Store longitude information in variable v_lon
    v_lon = v_buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    #  Print the information on the screen for all the active buses.
    print("Bus %d is at latitude %f and longitude %s" %(i,v_lat,v_lon))
