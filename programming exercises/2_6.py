amount_bay = float(input('Введите сумму покупки: '))
fed_tax = amount_bay * 0.05
reg_tax = amount_bay * 0.025

print(f'Сумма покупки равна: {amount_bay:,.2f}',
      f'Федеральный налог составил: {fed_tax:,.2f}',
      f'Региональный налог составил: {reg_tax:,.2f}',
      f'Общий налог с продаж составил: {fed_tax + reg_tax:,.2f}',
      f'Сумма к оплате: {amount_bay + fed_tax + reg_tax:,.2f}', sep='\n')