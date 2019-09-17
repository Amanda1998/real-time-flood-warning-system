"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key
from .stationdata import build_station_list
from .station import MonitoringStation
from .utils import sorted_by_key
from .haversine import haversine
from . import datafetcher
from operator import itemgetter

def rivers_with_station(stations):
    """return all river with a monitoring station"""
    R = set() #create an empty set for river
    
    """add river names to the set"""
    for station in stations:
        R.add(station.river)
    return sorted(R)
    
def stations_by_river(stations):
    """maps river to the station"""
    
    rivers = rivers_with_station(stations)
    s_dict = {}
    #N = list()  #empty set for station names   
    for river in rivers:
        #loop river list
        
        N = []
        for station in stations:
            if station.river == river:
                N.append(station.name)
        N_1 = sorted (N)
        s_dict.update({river:list(N_1)})
    
    return s_dict


def rivers_by_station_number(stations,N):   
    #tations = build_station_list()
    rivers = rivers_with_station(stations)
    #print(rivers)
    
    stations_to_rivers = stations_by_river(stations)
    #print(stations_to_rivers.values())
    
    rank_0 = set()
    for key,value in  stations_to_rivers.items():
        station_list = list(value)
        n = len(station_list)
        a = (key, n) 
        #print(a)
        rank_0.add(a)
    
    rank_1 = list(rank_0)
    rank = sorted(rank_1,key=itemgetter(1), reverse = True)  
    # print(rank)
    n = N 
    
    while rank[n][1] == rank[n-1][1]:
        print(n, rank[n][1], rank[n+1][1])
        n += 1
                   
    return (rank[0:n])
   

def stations_by_distance(stations, p):
    distances = map(lambda s: (s, haversine(p, s.coord)), stations)
    return sorted_by_key(distances, 1)

def stations_within_radius(stations, centre, r):
    return filter(lambda s: haversine(centre, s.coord) < r, stations)