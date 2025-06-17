amount_pay = float(input('Введите стоимость заказа: '))
tax = amount_pay * 0.07
tips = amount_pay * 0.18
total = amount_pay + tax + tips
print(f'Счёт за еду составил: {amount_pay:,.2f}',
      f'налог: {tax:,.2f}',
      f'чаевые: {tips:,.2f}',
      f'итоговый счёт равен: {total:,.2f}', sep='\n')