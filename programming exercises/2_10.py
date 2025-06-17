from  time import sleep
number_of_buns = int(input('Сколь булочек вы хотите испечь?: '))
sugar = 1.5
oil = 1
flour = 2.75
STANDARD_UNIT = 48
ratio = number_of_buns / STANDARD_UNIT
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print(f'Дла приготовления булочек в количестве: {number_of_buns} шт., вам примерно понадобится: ',
      f'сахар: {sugar * ratio:.1f} стакан(а,ов)',
      f'масло: {oil * ratio:.1f} стакан(а,ов)',
      f'мука: {flour * ratio:.2f} стакан(а,ов)', sep='\n')