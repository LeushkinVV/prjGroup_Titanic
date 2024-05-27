import matplotlib.pyplot as plt
import streamlit as st
import csv
def var12_main():
    st.title('Отсутствие данных о пассажирах')
    st.write('Для просмотра информации о количестве пассажиров, по которым нет данных, выберите соответствующую категорию')
    choice = st.selectbox('Выберите категорию:', ['PassengerId',	'Survived',	'Pclass',	'Name',	'Sex',	'Age',	'SibSp','Parch',	'Ticket',	'Fare',	'Cabin',	'Embarked'])

    columns = ['PassengerId',	'Survived',	'Pclass',	'Name',	'Sex',	'Age',	'SibSp',
               'Parch',	'Ticket',	'Fare',	'Cabin',	'Embarked']

    index = columns.index(choice)

    with open('data.csv') as file:
        missing = 0
        total = 0
        val = 0
        reader = csv.reader(file)
        for line in reader:
            total += 1
            if line[index] == '':
                missing += 1
                val = missing / total * 100


    if choice == 'PassengerId':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Survived':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Pclass':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Name':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Sex':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Age':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%':val}
        st.table(data)
    if choice == 'SibSp':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Parch':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Ticket':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Fare':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Cabin':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)
    if choice == 'Embarked':
        data = {'Категория': choice, 'Количество пассажиров без данных': missing, 'Доля,%': val}
        st.table(data)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(choice, missing)
    plt.xlabel("Наименование категории")
    plt.ylabel("Количество пассажиров")
    plt.title("Количество пассажиров, по которым отсутствуют данные")
    st.pyplot(fig)
