import streamlit as st
import matplotlib.pyplot as plt


# def var17_main():
#     st.title("Cтоимость билета у пассажиров по каждому пункту посадки")
#     choice = st.selectbox('Выберите тип стоимости:', ['Минимальная', 'Средняя', 'Максимальная'])
#     with open("data.csv") as file:
#         next(file)
#         c_count = 0
#         s_count = 0
#         q_count = 0
#
#         c_sum = 0
#         s_sum = 0
#         q_sum = 0
#
#         c_max = 0
#         q_max = 0
#         s_max = 0
#
#         c_min = 100000
#         s_min = 100000
#         q_min = 100000
#
#         for line in file:
#             data = line.strip().split(',')
#             print("zz_01 {} file: {}".format(data[10], file))
#             if float(data[10]) == 0:
#                 continue
#             else:
#                 price = float(data[10])
#             if data[-1] == "C":
#                 c_count += 1
#                 c_sum += price
#                 if price < c_min:
#                     c_min = price
#                 if price > c_max:
#                     c_max = price
#             elif data[-1] == "S":
#                 s_count += 1
#                 s_sum += price
#                 if price < s_min:
#                     s_min = price
#                 if price > s_max:
#                     s_max = price
#             elif data[-1] == "Q":
#                 q_count += 1
#                 q_sum += price
#                 if price < q_min:
#                     q_min = price
#                 if price > q_max:
#                     q_max = price
#         avr_c = str(c_sum / c_count)
#         avr_s = str(s_sum / s_count)
#         avr_q = str(q_sum / q_count)
#         pclass = ['C', 'S', 'Q']
#         if choice == 'Минимальная':
#             min_price = [c_min, s_min, q_min]
#             data = {'Пункт отправления': pclass, 'Минимальная стоимость': min_price}
#             st.table(data)
#
#             fig = plt.figure(figsize=(10, 5))
#             plt.bar(pclass, min_price)
#             plt.xlabel("Пункты отправления")
#             plt.ylabel("Стоимость")
#             plt.title("Минимальная стоимость билетов по пунктам отправления")
#             st.pyplot(fig)
#         elif choice == 'Максимальная':
#             max_price = [c_max, s_max, q_max]
#             data = {'Пункт отправления': pclass, 'Максимальная стоимость': max_price}
#             st.table(data)
#
#             fig = plt.figure(figsize=(10, 5))
#             plt.bar(pclass, max_price)
#             plt.xlabel("Пункты отправления")
#             plt.ylabel("Стоимость")
#             plt.title("Максимальная стоимость билетов по пунктам отправления")
#             st.pyplot(fig)
#         elif choice == 'Средняя':
#             avr_price = [c_sum / c_count, s_sum / s_count, q_sum / q_count]
#             data = {'Пункт отправления': pclass, 'Средняя стоимость': avr_price}
#             st.table(data)
#
#             fig = plt.figure(figsize=(10, 5))
#             plt.bar(pclass, avr_price)
#             plt.xlabel("Пункты отправления")
#             plt.ylabel("Стоимость")
#             plt.title("Средняя стоимость билетов по пунктам отправления")
#             st.pyplot(fig)

def prices(lines, option):
    c_count = 0
    s_count = 0
    q_count = 0

    c_sum = 0
    s_sum = 0
    q_sum = 0

    c_max = 0
    q_max = 0
    s_max = 0

    c_min = 100000
    s_min = 100000
    q_min = 100000

    for line in lines:
        data = line.strip().split(',')
        fare = str(data[-3]).strip()
        embraked = str(data[-1]).strip()
        # if float(data[10]) == 0:
        if float(fare) == 0:
            continue
        else:
            price = float(fare)
        if embraked == "C":
            c_count += 1
            c_sum += price
            # print("price: {}".format(price))
            if price < c_min:
                c_min = price
            if price > c_max:
                c_max = price
        elif embraked == "S":
            s_count += 1
            s_sum += price
            if price < s_min:
                s_min = price
            if price > s_max:
                s_max = price
        elif embraked == "Q":
            q_count += 1
            q_sum += price
            if price < q_min:
                q_min = price
            if price > q_max:
                q_max = price
    if option == 0:
        return [c_min, s_min, q_min]
    elif option == 1:
        return [c_max, s_max, q_max]
    elif option == 2:
        return [c_sum / c_count, s_sum / s_count, q_sum / q_count]

def var17_main_2():
    st.title("Cтоимость билета у пассажиров по каждому пункту посадки")
    choice = st.selectbox('Выберите тип стоимости:', ['Минимальная', 'Средняя', 'Максимальная'])
    lines = []
    with open("data.csv") as file:
        next(file)
        lines = file.readlines()

    pclass = ['C', 'S', 'Q']
    if choice == 'Минимальная':
        min_price = prices(lines,0)
        data = {'Пункт отправления': pclass, 'Минимальная стоимость': min_price}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(pclass, min_price)
        plt.xlabel("Пункты отправления")
        plt.ylabel("Стоимость")
        plt.title("Минимальная стоимость билетов по пунктам отправления")
        st.pyplot(fig)
    elif choice == 'Максимальная':
        max_price = prices(lines, 1)
        data = {'Пункт отправления': pclass, 'Максимальная стоимость': max_price}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(pclass, max_price)
        plt.xlabel("Пункты отправления")
        plt.ylabel("Стоимость")
        plt.title("Максимальная стоимость билетов по пунктам отправления")
        st.pyplot(fig)
    elif choice == 'Средняя':
        avr_price = prices(lines,2)
        data = {'Пункт отправления': pclass, 'Средняя стоимость': avr_price}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(pclass, avr_price)
        plt.xlabel("Пункты отправления")
        plt.ylabel("Стоимость")
        plt.title("Средняя стоимость билетов по пунктам отправления")
        st.pyplot(fig)

# var17_main()
var17_main_2()
