from var14 import work



def test_work_1():
    lines = [
        '6,0,male,,3,0,330877,8.4583,,Q',
        '7,0,male,54,0,0,17463,51.8625,E46,S',
        '8,0,male,2,3,1,349909,21.075,,S'
    ]
    assert work(lines) == (0, 0, 7, 0)


def test_work_2():
    lines = [
        '6,1,,male,,0,1,330877,8.4583,,Q',
        '7,0,,male,54,0,0,17463,51.8625,E46,S',
        '8,0,,male,2,3,1,349909,21.075,,S'
    ]
    assert work(lines) == (1, 0, 4, 0)


def test_work_3():
    lines = [
        '9,0,,male,27,0,2,347742,11.1333,,S',
        '10,1,,female,14,1,0,237736,30.0708,,C',
        '11,1,female,4,1,1,PP 9549,16.7,G6,S'
    ]
    assert work(lines) == (0, 3, 2, 0)


def test_work_4():
    lines = [
        '12,1,female,58,0,1,113783,26.55,C103,S',
        '13,0,male,20,0,0,A/5. 2151,8.05,,S',
        '14,0,male,39,1,5,347082,31.275,,S'
    ]
    assert work(lines) == (0, 1, 6, 0)


def test_work_5():
    lines = [
        '15,0,female,14,5,2,350406,7.8542,,S',
        '16,1,female,55,1,0,248706,16,,S',
        '17,0,male,2,4,1,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 1, 5, 7)


def test_work_6():
    lines = [
        '15,0,female,14,5,a,350406,7.8542,,S',
        '16,1,female,55,1,0,248706,16,,S',
        '17,0,male,2,4,1,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 1, 5, 5)


def test_work_7():
    lines = [
        '15,0,female,14,5,2,350406,7.8542,,S',
        '16,,female,55,1,0,248706,16,,S',
        '17,0,male,2,4,1,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 0, 5, 7)


def test_work_8():
    lines = [
        '15,0,female,14,5,2,350406,7.8542,,S',
        '16,,female,55,1,0,248706,16,,S',
        '17,0,,2,4,1,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 0, 0, 7)


def test_work_9():
    lines = [
        '15,0,ЫЫЫ,14,5,2,350406,7.8542,,S',
        '16,,female,55,1,0,248706,16,,S',
        '17,0,male,2,4,1,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 0, 5, 0)


def test_work_10():
    lines = [
        '15,1,female,14,5,2,350406,7.8542,,S',
        '16,,female,55,1,0,248706,16,,S',
        '17,0,male,2,4,1,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 7, 5, 0)


def test_work_11():
    lines = [
        '15, 1,female,14,    5,2,350406,7.8542,,S',
        '16,,female,55,1,0,248706,16,,S',
        '17,0,male,2,4,1  ,382652,29.125,,Q'
    ]
    assert work(lines) == (0, 7, 5, 0)
