PRICE_A = 1.50
PRICE_B = 3.00
PRICE_C = 4.00
PRICE_D = 4.75

GRADE_A = 200
GRADE_B = 600
GRADE_C = 1000

weight = int(input('Введите вес посылки в граммах: '))

if weight > GRADE_C:
    price_mail = weight * PRICE_D
    print(f'Сумма отправки составляет: {price_mail:,.2f}')
elif weight > GRADE_B and weight <= GRADE_C:
    price_mail = weight * PRICE_C
    print(f'Сумма отправки составляет: {price_mail:,.2f}')
elif weight > GRADE_A and weight <= GRADE_B:
    price_mail = weight * PRICE_B
    print(f'Сумма отправки составляет: {price_mail:,.2f}')
elif weight <= GRADE_A:
    price_mail = weight * PRICE_A
    print(f'Сумма отправки составляет: {price_mail:,.2f}')
else:
    print('Что то пошло не так, извините')