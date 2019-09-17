#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:28:33 2018

@author: amandahu
"""

from analyse.stationdata import build_station_list
from analyse.geo import rivers_with_station,stations_by_river,rivers_by_station_number

def run():
    stations = build_station_list()
    print(rivers_by_station_number(stations,9))
    
    
      

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IB Flood Warning System ***")
    run()
