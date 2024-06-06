from var12 import get_empty_data


def test_get_empty_data():
    lines = ['1,2,3,4,5,6,7,8',
             '1,2,3,5,0,'',0,0',
             '1,2,0,5,8,'','',0',
             '0,0,0,0,0,0,0,0', ]
    assert get_empty_data(lines,5) == (2, 50)


def test_get_empty_data_2():
    lines = ['1,2,3,4,5,6,7,8',
             '1,2,3,5,0,'',0,0',
             '1,2,0,5,8,'','',0',
             '0,0,0,'',0,0,0,0', ]
    assert get_empty_data(lines,4) == (0, 0)


def test_get_empty_data_3_false():
    lines = ['1,2,3,4,5,6,7,8',
             '1,2,3.2,5,0,'',0,0',
             '1,2,0,5,8,'','',0',
             '0,0,0,0,0,0,0,0', ]
    assert get_empty_data(lines,2) == (0, 0)
    
