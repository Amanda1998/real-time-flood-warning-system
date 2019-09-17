#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:42:15 2018

@author: amandahu
"""

from analyse.stationdata import build_station_list
from analyse.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))
    
    
      

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IB Flood Warning System ***")
    run()
