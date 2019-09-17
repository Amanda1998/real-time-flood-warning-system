from analyse.stationdata import build_station_list
from analyse.geo import stations_by_distance

CAMBRIDGE_COORDINATES = (52.2053, 0.1218)

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    distances = stations_by_distance(stations, CAMBRIDGE_COORDINATES)

    sorted_distances = list(map(lambda d: (d[0].name, d[0].town, d[1]), distances))
    print(sorted_distances[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()


