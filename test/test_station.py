"""Unit test for the station module"""

import pytest
from analyse.station import MonitoringStation,inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    latest_level = 3.00
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = latest_level

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    
    wrong_data_1 = (9.0, 3.0)
    wrong_data_2 = None
    
    s1 = MonitoringStation(s_id, m_id, label, coord, wrong_data_1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, wrong_data_2, river, town)

    
    assert s.typical_range_consistent() == True
    assert s1.typical_range_consistent() == False
    assert s2.typical_range_consistent() == False

    assert s.relative_water_level() == (3.00 + 2.3)/(3.4445 + 2.3)
    assert s.warning_level() == "severe"
    l = list()
    l.append(s1)
    station_wrong_data = inconsistent_typical_range_stations(l)
   # print(station_wrong_data)
    assert station_wrong_data == ["some station"]
    
    