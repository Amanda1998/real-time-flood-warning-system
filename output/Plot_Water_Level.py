import datetime
from analyse.stationdata import build_station_list, update_water_levels
from analyse.datafetcher import fetch_measure_levels
from analyse.flood import stations_highest_rel_level
from analyse.plot import plot_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 5)

    dt = 10

    for s in highest_stations:
        dates, levels = fetch_measure_levels(s[0].measure_id, dt=datetime.timedelta(days=dt))
        # print(dates, levels)
        plot_water_levels(s[0], dates, levels)

if __name__ == "__main__":
    run()

