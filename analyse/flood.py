from analyse.station import MonitoringStation
from analyse.stationdata import build_station_list, update_water_levels
from analyse.utils import sorted_by_key
from operator import itemgetter
def station_level_over_threshold(stations,tol):
    dangerous_station_list =[]
    for station in stations:
        ratio = station.relative_water_level()
        if ratio is not None:
            if ratio <= tol:
                pass
            else:
                a = [station, ratio]
                dangerous_station_list.append(a)
    return sorted(dangerous_station_list,key=itemgetter(1), reverse = True)

def stations_highest_rel_level(stations, N):
    highest_rel_level_station_list = []
    for station in stations:
        ratio = station.relative_water_level()
        if ratio is not None:
            a = [station, ratio]
            highest_rel_level_station_list.append(a)
    sorted_list_of_rel_level = sorted(highest_rel_level_station_list,key=itemgetter(1), reverse = True)
    warning_list = sorted_list_of_rel_level[0: N]
    return warning_list
