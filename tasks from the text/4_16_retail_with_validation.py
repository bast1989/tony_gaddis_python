# Эта программа вычисляет розничные цены.
MARK_UP = 2.5   # Процент надбавки.
another = 'д'   # Переменная управления циклом.

# Обработать один или несколько товаров.
while another == 'д' or another == 'Д':
    # Получить оптовую стоимость товара.
    wholesale = float(input('Bвeдитe оптовую стоимость вара: '))

    # Проверить допустимость оптовой стоимости.
    while wholesale < 0:
        print('ОШИБКА: стоимость не может быть отрицательной.')
        wholesale = float(input('Bвeдитe правильную' +
                                'оптовую стоимость: '))

    # Вычислить розничную цену.
    retail = wholesale * MARK_UP

    # Показать розничную цену.
    print(f'Розничная цена товара: {retail:,.2f}')

    # Повторить?
    another = input('Ecть еще один товар? ' +
                    '(Введите д, если да): ')
