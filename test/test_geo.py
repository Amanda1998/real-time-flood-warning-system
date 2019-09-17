#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:32:05 2018

@author: amandahu
"""

import pytest
from analyse.stationdata import build_station_list
import analyse.geo
from operator import itemgetter

def test_rivers_with_station ():
    stations = build_station_list()
    test_set = analyse.geo.rivers_with_station(stations)
    assert type(test_set) == list
#    l = list(test_set)
#    assert l[0:10] == "['Addlestone Bourne', 'Adur', 'Aire Washlands', 'Alconbury Brook', 'Aldbourne', 'Aller Brook', 'Alre', 'Alt', 'Alverthorpe Beck', 'Ampney Brook']"

def test_stations_by_river():
    stations = build_station_list()
    test_dict = analyse.geo.stations_by_river(stations)
    assert type(test_dict) == dict
    
def test_rivers_by_station_number():
    stations = build_station_list()
    test_object = analyse.geo.rivers_by_station_number(stations, 9)
    assert type(test_object) == list
#    assert test_object == "[('Thames', 55), ('River Avon', 31), ('River Great Ouse', 30), ('River Aire', 21), ('River Calder', 21), ('River Severn', 20), ('River Derwent', 18), ('River Stour', 17), ('River Wharfe', 15)]"   
#    
def test_stations_within_radius():
    stations = build_station_list()
    test_list1 = analyse.geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert type(test_list1) == filter

def test_stations_by_distance():
    stations = build_station_list()
    test_list2 = analyse.geo.stations_by_distance(stations, (52.2053, 0.1218))
    assert type(test_list2) == list
