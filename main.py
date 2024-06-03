# Это работа по «Программной инженерии»
# Группы: 2023-ФГиИБ-ПИ-1см
# Практическое занятие №11. Групповая работа
# Студентов:
# 1. Леушкин Виталий Владимирович
#       Вариант 7: "Найти средний возраст пассажиров по
#       каждому классу обслуживания (поле Pclass,
#       указав количество братьев, сестер... (столбец SibSp): [0, …, 8]."
# 2. Грачева Елена Викторовна
#       Вариант 11: "Вычислить долю погибших и спасенных пассажиров,
#       указав возрастную категорию из списка - «молодой» (до 30 лет),
#       «среднего возраста» (от 30 до 60) и «старый» (более 60 лет)"
# 3. Куницына Юлия Валерьевна
#       Вариант 12: "Подсчитать количество и процент пропусков в данных
#       для указанного столбца (из списка)"
# 4. Борисов Константин Александрович
#       Вариант 14: "Посчитать число родственников отдельно для выживших
#       и погибших пассажиров указанного пола"
# 5. Старновкина Любовь Викторовна
#       Вариант 17: "Вычислить среднюю, минимальную или максимальную (выбрать
#       из списка) стоимость билета у пассажиров по каждому пункту посадки"


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
variants = [
    'Вариант 7',
    'Вариант 11',
    'Вариант 12',
    'Вариант 14',
    'Вариант 17'
]
variants_text = {
    'Вариант 7': 'Вариант 7: \"Найти средний возраст пассажиров по каждому '
    'классу обслуживания (поле Pclass, указав количество братьев,'
    'сестер... (столбец SibSp): [0, …, 8].\"',
    'Вариант 11': 'Вариант 11: \"Вычислить долю погибших и спасенных'
    'пассажиров, указав возрастную категорию из списка - \"молодой\" '
    '(до 30 лет), \"среднего возраста\" (от 30 до 60) и \"старый\" (более'
    ' 60 лет)\"',
    'Вариант 12': 'Вариант 12: \"Подсчитать количество и процент пропусков'
    'в данных для указанного столбца (из списка)\"',
    'Вариант 14': 'Вариант 14: \"Посчитать число родственников отдельно для'
    'выживших и погибших пассажиров указанного пола\"',
    'Вариант 17': 'Вариант 17: \"Вычислить среднюю, минимальную или максимальную'
    ' (выбрать из списка) стоимость билета у пассажиров по каждому пункту посадки\"'
}

chois = st.selectbox('Выберите вариант работы', ['выберите вариант']+variants)
st.text('')

if chois == 'выберите вариант':
    st.info('Выберите вариант из выпадающего списка!')
else:
    st.info(f'Представлен {variants_text[chois]}')
    if chois == variants[0]:
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
        st.error(f'Вариант \"{chois}\" пока не реализован, выберите'
                 'другой вариант из выпадающего списка!')
