import pytest
from analyse.flood import station_level_over_threshold, stations_highest_rel_level
from analyse.station import MonitoringStation



def analysis_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label_1 = "station_1"
    label_2 = "station_2"
    label_3 = "station_3"
    label_4 = "station_4"
    coord = (-2.0, 4.0)
    trange = (0, 10)
    river = "River X"
    town = "My Town"
    latest_level_1 = 5.0
    latest_level_2 = 3.0
    latest_level_3 = 6.0
    latest_level_4 = 11.0
    s1 = MonitoringStation(s_id, m_id, label_1, coord, trange, river, town)
    s1.latest_level = latest_level_1
    s2 = MonitoringStation(s_id, m_id, label_2, coord, coord, river, town)
    s2.latest_level = latest_level_2
    s3 = MonitoringStation(s_id, m_id, label_3, coord, coord, river, town)
    s3.latest_level = latest_level_3
    s4 = MonitoringStation(s_id, m_id, label_4, coord, coord, river, town)
    s4.latest_level = latest_level_4
    fake_station_list = [s1,s2,s3,s4]

    a = analysis_station(fake_station_list,"moderate")
    assert a == [["station_1" , "moderate"]]
    b = analysis_station(fake_station_list,"low")
    assert b == [["station_2" , "low"]]
    c = analysis_station(fake_station_list,"high")
    assert c == [["station_3" , "high"]]
    d = analysis_station(fake_station_list,"severe")
    assert d == [["station_2" , "severe"]]