YEARS = 5
PAY = 145000
UP = 0.03
pay = 145000

up_pay = PAY * UP

for y in range(YEARS):
    print(f'Год обучения {y + 1} - Оплата {pay:,.2f}')
    pay += up_pay