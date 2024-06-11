import matplotlib.pyplot as plt
import streamlit as st



def var14_main():
    lines = get_data(filename)
    sum_life_m, sum_life_f, sum_dead_m, sum_dead_f = work(lines)
    show_web(sum_life_m, sum_life_f, sum_dead_m, sum_dead_f)


filename = "data.csv"


def show_web(sum_life_m, sum_life_f, sum_dead_m, sum_dead_f):
    data = ""
    option = st.selectbox('Пол:', ['Мужской', 'Женский'])
    if option == 'Мужской':
        data = {'тип': ['Родственников у выживших',
                        'Родственников у погибших'],
                'данные': [sum_life_m, sum_dead_m]}
    elif option == 'Женский':
        data = {'тип': ['Родственников у выживших',
                        'Родственников у погибших'],
                'данные': [sum_life_f, sum_dead_f]}

    st.dataframe(data)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(data['тип'], data['данные'])
    xlab = "Пол {}".format(option)
    plt.xlabel(xlab)
    plt.ylabel("Колличество родственников")
    plt.title("Колличество родственников у выживших и погибших пассажиров")
    st.pyplot(fig)


def get_data(fn):
    with open(fn) as file:
        lines = file.readlines()
    return lines[1:]


def work(lines):
    sum_life_m = 0
    sum_life_f = 0
    sum_dead_m = 0
    sum_dead_f = 0
    for line in lines:
        tmpr = line.strip().rsplit(",", 8)
        tmp = line.strip().split(",", 3)
        who = isdigit(tmp[1], -1)
        sibsp = isdigit(tmpr[3])
        sex = tmpr[1]
        parch = isdigit(tmpr[4])
        if who == 0:
            if sex == 'male':
                sum_dead_m = sum_dead_m + sibsp + parch
            elif sex == 'female':
                sum_dead_f = sum_dead_f + sibsp + parch
        if who == 1:
            if sex == 'male':
                sum_life_m = sum_life_m + sibsp + parch
            elif sex == 'female':
                sum_life_f = sum_life_f + sibsp + parch
    return sum_life_m, sum_life_f, sum_dead_m, sum_dead_f


def isdigit(val, result=0):
    if str(val).strip().isdigit():
        return int(val)
    return result
