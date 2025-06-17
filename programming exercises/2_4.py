buy_1 = float(input('Введите стоимость первого товара: '))
buy_2 = float(input('Введите стоимость второго товара: '))
buy_3 = float(input('Введите стоимость третьего товара: '))
buy_4 = float(input('Введите стоимость четвёртого товара: '))
buy_5 = float(input('Введите стоимость пятого товара: '))

amount_buy = buy_1 + buy_2 + buy_3 + buy_4 + buy_5
tax = amount_buy * 0.07
total = amount_buy + tax
print(f'Вы приобрели товаров на сумму: {amount_buy:,.2f}',
      f'\nСумма налога на приобретённый товар составит: {tax:,.2f}',
      f'\nИтоговая сумма к оплат: {total:,.2f}')