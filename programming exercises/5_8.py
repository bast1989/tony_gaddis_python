PAINT = 5
WORK_HOURS = 8
SQUARE = 10
PRICE = 2000


def calculate(total_square, price_paint):
    if total_square <= SQUARE:
        print('Необходимо:')
        print(f'Литров краски: {PAINT}')
        print(f'Часов работы: {WORK_HOURS}')
        print(f'Краска стоит: {price_paint}')
        print(f'Работа стоит: {PRICE}')
        print(f'Общая стоимость: {PRICE + price_paint}')
    else:
        if total_square % SQUARE != 0:
            unit_square = total_square // 10 + 1
            print('Необходимо:')
            print(f'Литров краски: {PAINT * unit_square}')
            print(f'Часов работы: {WORK_HOURS * unit_square}')
            print(f'Краска стоит: {price_paint * unit_square}')
            print(f'Работа стоит: {PRICE * unit_square}')
            print(f'Общая стоимость: {PRICE * unit_square + price_paint * unit_square}')
        else:
            unit_square = total_square / 10
            print('Необходимо:')
            print(f'Литров краски: {PAINT * unit_square}')
            print(f'Часов работы: {WORK_HOURS * unit_square}')
            print(f'Краска стоит: {price_paint * unit_square}')
            print(f'Работа стоит: {PRICE * unit_square}')
            print(f'Общая стоимость: {PRICE * unit_square + price_paint * unit_square}')




def main():
    total_square = int(input('Введите площадь окрашиваемой стены: '))
    price_paint = float(input('Введите стоимость краски: '))
    calculate(total_square, price_paint)


if __name__ == '__main__':
    main()
