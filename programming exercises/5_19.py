def calculate(money, rate, month):
    return money * ((1 + rate) ** month)


def main():
    money = int(input('Введите сумму вклада: '))
    rate = (int(input('Введите процентную ставку: '))) / 100
    month = int(input('Введите количество месяцев вклада: '))

    print(f'Суммы на счету составит: {calculate(money, rate, month):,.2f}')


if __name__ == '__main__':
    main()