from analyse.flood import station_level_over_threshold
from analyse.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    dangerous_stations = station_level_over_threshold(stations,0.8)
    print (list(map(lambda s: [s[0].name, s[1]], dangerous_stations)))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()