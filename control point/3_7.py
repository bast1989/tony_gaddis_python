sale = float(input('Введите сумму продаж: '))
commission_rate = 0

if sale >= 10000:
    commission_rate = 0.2

print(f'Комиссия с продаж равна: {commission_rate}')