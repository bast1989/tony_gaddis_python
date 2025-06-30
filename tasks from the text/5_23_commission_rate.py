# Эта программа вычисляет выплату продавцу
# в компании 'Создай свою музыку'.

# Функция get sales получает от пользователя
# месячные продажи продавца и возвращает это значение.
def get_sales():
    # Получить сумму месячных продаж.
    sales = float(input('Введите сумму продаж: '))
    # Вернуть введенную сумму.
    return sales


# Функция get_advanced_pay получает сумму
# авансовой выплаты конкретному продавцу
# и возвращает эту сумму.
def get_advanced_pay():
    # Получить сумму авансовой выплаты.
    print('Введите авансовый платёж',
          'Если авансового платежа',
          'не было введите 0', sep='\n', end='')
    advanced_pay = float(input(': '))
    # Вернуть введенную сумму.
    return advanced_pay


# Функция determine_comm_rate принимает сумму продаж
# в качестве аргумента и возвращает подходящую
# ставку комиссионных.
def determine_comm_rate(sales):
    # Определить ставку комиссионных.
    if sales <= 10000:
        comm_rate = 0.10
    elif sales > 10000 and sales <= 15000:
        comm_rate = 0.12
    elif sales > 15000 and sales <= 18000:
        comm_rate = 0.14
    elif sales > 18000 and sales <= 22000:
        comm_rate = 0.16
    else:
        comm_rate = 0.18
    # Вернуть ставку комиссионных.
    return comm_rate


def main():
    # Получить сумму продаж.
    sales = get_sales()

    # Получить сумму авансовой оплаты.
    advanced_pay = get_advanced_pay()

    # Определить ставку комиссионных.
    comm_rate = determine_comm_rate(sales)

    # Рассчитать оплату.
    pay = sales * comm_rate - advanced_pay

    # Показать сумму выплаты.
    print(f'Выплата составляет ${pay:,.2f}')

    # Определить, является ли выплата отрицательной.
    if pay < 0:
        print('Продавец должен возместить разницу')
        print('компании.')



if __name__ == '__main__':
    main()



