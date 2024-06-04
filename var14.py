import matplotlib.pyplot as plt
import streamlit as st


def var14_main():
    lines = get_data(filename)
    sum_life_m, sum_life_f, sum_dead_m, sum_dead_f = work(lines)
    show_web(sum_life_m, sum_life_f, sum_dead_m, sum_dead_f)


filename = "data.csv"


def show_web(sum_life_m, sum_life_f, sum_dead_m, sum_dead_f):
    data = ""
    st.header('Данные пассажиров Титаника')
    st.write('Для просмотра числа родственников у выживших и погибших пассажиров, выберите пол пассажира')
    option = st.selectbox('Значение поля Sex:', ['Мужской', 'Женский'])
    if option == 'Мужской':
        data = {'тип': ['Родственников у выживших', 'Родственников у погибших'], 'данные': [sum_life_m, sum_dead_m]}
    elif option == 'Женский':
        data = {'тип': ['Родственников у выживших', 'Родственников у погибших'], 'данные': [sum_life_f, sum_dead_f]}

    st.table(data)

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
        # Пропускаем первую строку
        # Разбиваю на столбцы
        tmpR = line.strip().rsplit(",", 8)
        tmp = line.strip().split(",", 3)
        # print("tmp: {}".format(tmp[:3]))
        # print("tmpR: {}".format(tmpR[1:]))
        # Считаем выживших и погибших
        who = -1
        # if tmp[1].isdigit():
        if str(tmp[1]).strip().isdigit():
            who = int(tmp[1])
        # print("who: {}".format(who))
        # количество братьеев, сестер в т.ч. сводных
        sibsp = 0
        if str(tmpR[3]).strip().isdigit():
            sibsp = int(tmpR[3])

        # количество родителей и детей
        parch = 0
        if str(tmpR[4]).strip().isdigit():
            parch = int(tmpR[4])

        sex = tmpR[1]

        # print("who: {} sibsp: {} Prach: {} sex: {}".format(who,sibsp, parch, sex))
        # if who.isdigit():
        # Суммируем родственников выживших и погибших
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


# lines = get_data(filename)
# # print(lines)
#
# sum_life_m, sum_life_f, sum_dead_m, sum_dead_f = work(lines)
#
# # print("Родственников у погибших: m {} - f {}".format(sum_dead_m,sum_dead_f))
# # print("Родственников у выживших: m {} - f {}".format(sum_life_m, sum_life_f))
#
# show_web(sum_life_m, sum_life_f, sum_dead_m, sum_dead_f)


# var14_main()
