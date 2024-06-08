import matplotlib.pyplot as plt
import streamlit as st


def get_empty_data(lines, index):
    miss = 0
    total = len(lines)
    val = 0
    for line in lines:
        lst = line.strip().split(',')
        if lst[index] == '':
            miss += 1
            val = miss / total * 100
    return miss, val


def var12_main():
    columns = ['PassengerId',	'Survived',	'Pclass',	'Name', 'Sex',
               'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    choice = st.selectbox('Выберите категорию:', columns)
    index = columns.index(choice)

    if index > 3:
        index += 1

    with open('data.csv') as file:
        lines = file.readlines()[1:]

    miss, val = get_empty_data(lines, index)
    st.dataframe({'Категория': ['Количество пассажиров без данных', 'Доля,%'],
                  'Данные': [miss, val]})
    if miss > 0:
        fig = plt.figure(figsize=(10, 5))
        plt.bar(['Количество,шт.', 'Доля,%'], [miss, val])
        plt.ylabel('Данные')
        plt.title("Количество и доля пассажиров, по которым отсутствуют данные")
        st.pyplot(fig)
