get_program_pack = int(input('Введите количество приобретённых лицензий: '))
price = 99

full_price = get_program_pack * price

if get_program_pack <= 9:
    discount = 0
    print(f'Вами куплено пакетов: {get_program_pack}',
          f'Сумма скидки составила: {discount:,.2f}$',
          f'К оплате {full_price - discount:,.2f}$.', sep='\n')
elif get_program_pack >= 10 and get_program_pack <= 19:
    discount = full_price * 0.1
    print(f'Вами куплено пакетов: {get_program_pack}',
          f'Сумма скидки составила: {discount:,.2f}$',
          f'К оплате {full_price - discount:,.2f}$.', sep='\n')
elif get_program_pack >= 20 and get_program_pack <= 49:
    discount = full_price * 0.2
    print(f'Вами куплено пакетов: {get_program_pack}',
          f'Сумма скидки составила: {discount:,.2f}$',
          f'К оплате {full_price - discount:,.2f}$.', sep='\n')
elif get_program_pack >= 50 and get_program_pack <= 99:
    discount = full_price * 0.3
    print(f'Вами куплено пакетов: {get_program_pack}',
          f'Сумма скидки составила: {discount:,.2f}$',
          f'К оплате {full_price - discount:,.2f}$.', sep='\n')
elif get_program_pack >= 100:
    discount = full_price * 0.4
    print(f'Вами куплено пакетов: {get_program_pack}',
          f'Сумма скидки составила: {discount:,.2f}$',
          f'К оплате {full_price - discount:,.2f}.$', sep='\n')
else:
    print('Что то пошло не так, извините.')
