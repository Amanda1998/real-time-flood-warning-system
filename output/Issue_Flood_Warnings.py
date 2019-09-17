
from analyse.stationdata import build_station_list, update_water_levels

def analysis_station(stations, level):
    b =[]
    for station in stations:
        level_1 = station.warning_level()
        if level_1 == level:
            b.append([station.name, level])
    return b

def run():
    stations = build_station_list()
    update_water_levels(stations)
    output = analysis_station(stations, "severe")
    print (output)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()


