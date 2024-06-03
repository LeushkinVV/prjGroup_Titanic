# Это работа по «Программной инженерии»
# Студент: Леушкин Виталий Владимирович
# Группа: 2023-ФГиИБ-ПИ-1см
# Практическое занятие №9. Веб-приложения с бибилиотекой streamlit
# Вариант 7: "Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass,
# указав количество братьев, сестер... (столбец SibSp): [0, …, 8]."

import matplotlib.pyplot as pit
import streamlit as st


def get_avg(lines: [], sibsp: int):
# Определяем список сумм возрастов по классам пассажиров
    pclass_summ = {'1': 0, '2': 0, '3': 0}
# Определяем список количество пассажиров по классам
    pclass_count = {'1': 0, '2': 0, '3': 0}
    for i, line in enumerate(lines):
# Если первая строка - это заголовок пропускаем
        if i == 0:
            continue
# формируем список из строки с полями, деля строку по разделителю ','
        data = line.split(',')
# data[6] это поле Age, а data[7] это поле SibSp, если Age не пустое и SibSp равно фильтру sibsp, то
        if data[6] != "" and int(data[7]) == sibsp:
# data[2] это поле Pcalss, суммируем возраст по классу пассажиров
            pclass_summ[data[2]] += float(data[6])
# увеличиваем счетчик пассажиров по их классу
            pclass_count[data[2]] += 1
# возвращаем список среднего возраста по классу пассажиров
# round(0.00000, 2) - округление до двух знаков после запятой
# конструкция IF одной строкой:
# val0 = <значение если истино> if <условие> else <значение если ложь>
    return \
        [
           round(pclass_summ['1']/pclass_count['1'] if pclass_count['1'] > 0 else 0.0,2),
           round(pclass_summ['2']/pclass_count['2'] if pclass_count['2'] > 0 else 0.0,2),
           round(pclass_summ['3']/pclass_count['3'] if pclass_count['3'] > 0 else 0.0,2)
        ]


def var7_main():
    st.header('Данные пассажиров Титаника')
    # выводим текст
    st.write('Для просмотра данных о среднем возрасте пассажиров по каждому классу обслуживания в соответствии с количеством братьев, сестер, сводных братьев, сводных сестер, супругов на борту,выберите соответствующий пункт из списка')

    # Определяем элемент управления number_input
    ss = st.number_input('Значение поля SibSp:', 0, 8, 0, 1)
    # вычисляем средний возраст пассажтиров по классам в соответствии с фильтром из number_input
    
# открываем файл
    with open('data.csv') as file:
# lines - список строк, читаем в lines файл
        lines = file.readlines()
# возвращаем среднее значение возраста по классам с учетом заданного фильтра sibsp
    avg_age = get_avg(lines, ss)

    # определяем подписи для таблицы и графика в виде списков
    pclass = ['1 класс', '2 класс', '3 класс']

    # определяем значения в виде словаря
    data = {'Класс обслуживания': pclass, 'Средний возраст': avg_age}
    # выводим таблицу
    mt = st.table(data)

    # определяем размер графика
    fig = pit.figure(figsize=(10, 5))
    # рисуем столбчатый график
    pit.bar(pclass, avg_age)
    # определяем название оси X
    pit.xlabel('Значение поля Pclass')
    # определяем название оси Y
    pit.ylabel('Возраст (поле Age)')
    # определяем название графика
    pit.title('Средний возраст пассажиров по классам обслуживания')
    # выводим столбчатый график
    st.pyplot(fig)
