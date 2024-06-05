import streamlit as st
import matplotlib.pyplot as plt


def prices(lines, option):
    counts = {'C': 0, 'S': 0, 'Q': 0}
    sums = {'C': 0, 'S': 0, 'Q': 0}
    max_prices = {'C': 0, 'S': 0, 'Q': 0}
    min_prices = {'C': float('inf'), 'S': float('inf'), 'Q': float('inf')}

    for line in lines:
        data = line.strip().split(',')
        price = float(data[-3])
        port = data[-1]

        if price == 0:
            continue

        if port in counts:
            counts[port] += 1
            sums[port] += price
            if price > max_prices[port]:
                max_prices[port] = price
            if price < min_prices[port]:
                min_prices[port] = price

    if option == 'min':
        return [min_prices['C'], min_prices['S'], min_prices['Q']]
    elif option == 'max':
        return [max_prices['C'], max_prices['S'], max_prices['Q']]
    elif option == 'avg':
        return [
            round(sums['C'] / counts['C'], 2) if counts['C'] != 0 else 0,
            round(sums['S'] / counts['S'], 2) if counts['S'] != 0 else 0,
            round(sums['Q'] / counts['Q'], 2) if counts['Q'] != 0 else 0
        ]


def var17_main():
    st.title("Стоимость билета у пассажиров по каждому пункту посадки")

    choice = st.selectbox('Выберите тип стоимости:',
                          ['Минимальная', 'Средняя', 'Максимальная'])
    option_map = {'Минимальная': 'min', 'Средняя': 'avg',
                  'Максимальная': 'max'}
    option = option_map[choice]

    with open("data.csv") as file:
        lines = file.readlines()[1:]
        prices_list = prices(lines, option)

    pclass = ['C', 'S', 'Q']
    data = {'Пункт отправления': pclass}

    if option == 'min':
        data['Минимальная стоимость'] = prices_list
        st.title("Минимальная стоимость билетов по пунктам отправления")
    elif option == 'max':
        data['Максимальная стоимость'] = prices_list
        st.title("Максимальная стоимость билетов по пунктам отправления")
    elif option == 'avg':
        data['Средняя стоимость'] = prices_list
        st.title("Средняя стоимость билетов по пунктам отправления")

    st.table(data)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(pclass, prices_list)
    plt.xlabel("Пункты отправления")
    plt.ylabel("Стоимость")
    plt.title(f"{choice} стоимость  билетов по пунктам отправления")
    st.pyplot(fig)
