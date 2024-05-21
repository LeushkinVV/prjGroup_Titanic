# Это работа по «Программной инженерии»
# Группы: 2023-ФГиИБ-ПИ-1см
# Практическое занятие №11. Групповая работа
# Студентов:
# 1. Леушкин Виталий Владимирович
#       Вариант 7: "Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass,
#       указав количество братьев, сестер... (столбец SibSp): [0, …, 8]."
# 2.
#

import streamlit as st
from var7 import var7_main
from var11 import var11_main
from var12 import var12_main
from var14 import var14_main
from var17 import var17_main

st.header('Практическое занятие №11')
# выводим картинку
st.image('titanic.jpg')
# выводим текст заголоака

st.header('Работа группы №3')
variants = ['Вариант 7', 'Вариант 11', 'Вариант 12', 'Вариант 14', 'Вариант 17']

chois = st.selectbox('Выберите вариант работы', ['выберите вариант']+variants)
st.text('')

if chois == 'выберите вариант':
    st.info(f'Выберите вариант из выпадающего списка!')
elif chois == variants[0]:
    st.info(f'Представлен {chois}')
    var7_main()
elif chois == variants[1]:
    var11_main()
elif chois == variants[2]:
    var12_main()
elif chois == variants[3]:
    var14_main()
elif chois == variants[4]:
    var17_main()
else:
    st.error(f'Вариант \"{chois}\" пока не реализован, выберите лругой вариант из выпадающего списка!')
