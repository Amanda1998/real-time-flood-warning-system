from analyse.flood import stations_highest_rel_level
from analyse.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    warning_stations = stations_highest_rel_level(stations, 10)
    print (list(map(lambda s: [s[0].name, s[1]], warning_stations)))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()