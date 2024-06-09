from var7 import get_avg


def test_get_avg_test_avg():
    lines = [
        ',,1,",",,12.2,0',
        ',,1,",",, 2.2,0',
        ',,2,",",,  32,0',
        ',,2,",",,  42,0',
        ',,3,",",,  22,0',
        ',,3,",",,44.2,0'
    ]
    assert get_avg(lines, 0) == [7.2, 37, 33.1]


def test_get_avg_test_age_false():
    lines = [
        ',,1,",",, 12.2,0',
        ',,1,",",,   -1,0',
        ',,2,",",,   32,0',
        ',,2,",",,   42,0',
        ',,3,",",,  -  ,0',
        ',,3,",",,"1,2",0',
        ',,3,",",, 44.2,0'
    ]
    assert get_avg(lines, 0) == [12.2, 37, 44.2]


def test_get_avg_test_pclass_in_not_1_2_3():
    lines = [
        ',,1,",",, 12.2,0',
        ',,1,",",,   -1,0',
        ',,2,",",,   32,0',
        ',,2,",",,   42,0',
        ',,3,",",,  -  ,0',
        ',,3,",",,"1,2",0',
        ',,3,",",, 44.2,0',
        ',,4,",",, 44.2,0',
        ',,0,",",, 44.2,0'
    ]
    assert get_avg(lines, 0) == [12.2, 37, 44.2]


def test_get_avg_test_filter():
    lines = [
        ',,1,",",,12.2,0',
        ',,1,",",, 2.2,1',
        ',,2,",",,  32,2',
        ',,2,",",,  42,3',
        ',,3,",",,  22,4',
        ',,3,",",,44.2,5'
    ]
    assert get_avg(lines, 0) == [12.2, 0, 0]
