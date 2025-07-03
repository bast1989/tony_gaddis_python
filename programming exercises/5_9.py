TAX_FED = 0.05
TAX_MUN = 0.025


def calculate(sales):
    print(f'Сумма муниципального налога: {sales * TAX_MUN}')
    print(f'Сумма федерального налога: {sales * TAX_FED}')
    print(f'Общий налог: {sales * TAX_MUN + sales * TAX_FED}')


def main():
    sales = float(input('Введите общий объём продаж: '))
    calculate(sales)


if __name__ == '__main__':
    main()