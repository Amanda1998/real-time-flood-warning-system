from analyse.stationdata import build_station_list
from analyse.geo import stations_within_radius

CAMBRIDGE_COORDINATES = (52.2053, 0.1218)

def run():
    stations = build_station_list()
    nearby_stations = stations_within_radius(stations, CAMBRIDGE_COORDINATES, 10)
    nearby_stations_names = map(lambda w: w.name, nearby_stations)

    print(sorted(nearby_stations_names))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()