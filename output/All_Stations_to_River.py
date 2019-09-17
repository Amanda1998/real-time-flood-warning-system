#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:28:24 2018

@author: amandahu
"""
from analyse.stationdata import build_station_list
from analyse.geo import rivers_with_station,stations_by_river

def run():
  stations = build_station_list()
  rivers = rivers_with_station(stations)
  stations_to_rivers = stations_by_river(stations)
  
  print (stations_to_rivers["River Aire"])
  print (stations_to_rivers["River Cam"])
  print (stations_to_rivers["Thames"])
  list_1 = list(stations_to_rivers)
  print (list_1[0:10])
 
  
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IB Flood Warning System ***")
    run()

