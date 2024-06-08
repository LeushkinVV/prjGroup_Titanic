from var17 import prices


def test_prices_test_min():
    lines = [

        '7.25,      ,S',
        '71.2833,   ,C',
        '7.925,     ,S',
        '53.1,      ,S',
        '8.05,      ,S',
        '8.4583,    ,Q',
        '51.8625,   ,S'
    ]
    option = 'min'  # Поиск минимальных стоимостей
    assert prices(lines, option) == [71.2833, 7.25, 8.4583]


def test_prices_test_max():
    lines = [
        '7.8958,      ,S',
        '27.7208,     ,C',
        '146.5208,    ,C',
        '7.75,        ,Q',
        '10.5,        ,S',
        '82.1708,     ,C',
        '52,          ,S'
    ]
    option = 'max'  # Поиск максимальных стоимостей
    assert prices(lines, option) == [146.5208, 52, 7.75]


def test_prices_test_avg():
    lines = [
        '7.7875,  ,Q',
        '8.6625,  ,S',
        '10.5,    ,S',
        '7.75,    ,Q',
        '46.9,    ,S',
        '27.7208, ,C',
        '73.5,    ,S',
        '14.4542, ,C',
        '56.4958, ,S',
        '7.65,    ,S'
    ]

    option = 'avg'  # Поиск средних стоимостей
    assert prices(lines, option) == [21.09, 33.95, 7.77]
