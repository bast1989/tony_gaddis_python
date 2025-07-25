# Эта программа вычисляет заработную плату до удержаний.

def main():
    try:
        # Почить количество отработанных часов.
        hours = int(input('Сколько часов вы отработали? '))

        # Получить почасовую ставку оплаты труда.
        pay_rate = float(input('Введите свою почасовую ставку: '))

        # Вычислить заработную плату до удержаний.
        gross_pay = hours * pay_rate

        # Показать заработную плату.
        print(f'Заработная плата: ${gross_pay:,.2f}')
    except ValueError as err:
        print('ОШИБКА: Отработанные часы и часовая ставка оплаты')
        print('должны быть допустимыми числами.')
        print(f'Текст ошибки: {err}')


if __name__ == '__main__':
    main()