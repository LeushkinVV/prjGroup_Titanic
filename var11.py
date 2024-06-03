import matplotlib.pyplot as plt
import streamlit as st


import matplotlib.pyplot as plt
import streamlit as st



def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
            if data[1] == "1":
                saved += 1
    return saved / total*100, (total - saved)  / total*100
with open('data.csv') as file:
    text = file.readlines()
    print(get_pas_count(text[1:], min_age =  0))

def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age) <= min_age + 30:
            total += 1
            if data[1] == "1":
                saved += 1
    return saved / total*100, (total - saved)  / total*100
with open('data.csv') as file:
    text = file.readlines()
    print(get_pas_count(text[1:],30))

def get_pas_count(lines, min_age):
    total = 0
    saved = 0

    for line in lines:
        data = line.split(',')
        age = data[6]
        if age != '' and min_age <= float(age):
            total += 1
            if data[1] == "1":
                saved += 1
    return saved / total*100, (total - saved)  / total*100
with open('data.csv') as file:
    text = file.readlines()

    print(get_pas_count(text[1:],60))


columns = ['до 30 лет', 'от 30 до 60 лет', 'старше 60 лет']
st.title('Пассажиры Титаника')
st.write('Для просмотра информации о доле выживших/погибших пассажиров выберите возраст:')
choice = st.selectbox('Выберите возраст:', columns)
index = columns.index(choice)


with open('data.csv') as file:
    lines = file.readlines()[1:]

min_age, val = get_pas_count(lines,index)
data = {'Возраст':['Выжившие', 'Погибшие'], 'Доля,%': [min_age,val]}
st.table(data)

x = [min_age]
y = [val]
plt.bar(choice, val)

fig = plt.figure(figsize=[10, 5])

plt.xlabel('Возраст пассажиров')
plt.ylabel('Доля выживших пассажиров')
plt.title('Диаграмма')
plt.legend()
st.pyplot(fig)
def var11_main():
    st.title('Пассажиры Титаника ')
    st.header('Доля погибших и спасенных пассажиров')
    st.subheader('Возрастная категория')
    st.markdown('1. «молодой» (до 30 лет)\n'
                '2. «среднего возраста» (от 30 до 60)\n'
                '3. «старый» (более 60 лет)\n')
    st.write('Чтобы узнать долю выживших в определенной возратной категории, выберите возраст')
    choise = st.selectbox('Выберете возраст:',
                          ["до 30 лет",
                        "от 30 до 60 лет",
                        "старше 60 лет"])
    x = ['до 30', 'от 30 до 60', 'от 60']
    y = [val1, val2, val3]
    tab = {'Возраст пассажиров': x, 'Доля погибших пассажиров': y}
    st.dataframe(tab)

    fig = plt.figure(figsize=[10, 5])
    plt.bar(x, y)
    plt.xlabel('Возраст пассажиров')
    plt.ylabel('Доля погибших пассажиров')
    plt.title('Диаграмма')
    plt.legend()
    st.pyplot(fig)
