import matplotlib.pyplot as plt
import streamlit as st

def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) < min_age + 30:
            total += 1
            if data[1] == "1":
               saved += 1
    return saved / total * 100, (total - saved) / total * 100

def var11_main():
    columns = ['до 30 лет', 'от 30 до 60 лет', 'старше 60 лет']
    st.title('Пассажиры Титаника')
    st.write('Для просмотра информации о доле выживших/погибших пассажиров выберите возраст:')
    choice = st.selectbox('Выберите возраст:', columns)
    index = columns.index(choice)

    with open('data.csv') as file:
        lines = file.readlines()[1:]

    min_age, val = get_pas_count(lines, index * 30)
    data = {'Возраст': ['Выжившие', 'Погибшие'], 'Доля,%': [min_age, val]}
    st.table(data)

    fig = plt.figure(figsize=[10, 5])
    plt.bar(choice, val)
    
    plt.xlabel('Возраст пассажиров')
    plt.ylabel('Доля выживших пассажиров')
    plt.title('Диаграмма')
    plt.legend()
    st.pyplot(fig)
