import pytest
from analyse.flood import station_level_over_threshold, stations_highest_rel_level
from analyse.station import MonitoringStation



def test_station_level_over_threshold():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0, 10)
    river = "River X"
    town = "My Town"
    latest_level = 5.0
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = latest_level
    wrong_data_1 = (9.0, 3.0)
    wrong_data_2 = None

    s1 = MonitoringStation(s_id, m_id, label, coord, wrong_data_1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, wrong_data_2, river, town)
    fake_station_list = [s,s1,s2]
    a = station_level_over_threshold(fake_station_list,0.4)
    a = list(map(lambda s: [s[0].name, s[1]], a))
    assert a == [["some station" , 0.5]]


def test_stations_highest_rel_level():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0, 10)
    river = "River X"
    town = "My Town"
    latest_level = 5.0
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = latest_level
    fake_station_list = [s]
    a = stations_highest_rel_level(fake_station_list,1)
    a = list(map(lambda s: [s[0].name, s[1]], a))
    assert a == [["some station" , 0.5]]


