# Эта программа преобразует скорости от 60
# до 130 км/ч (с приращениями в 10 км)
# в mph.

START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

print('KPH\t\tMPH')
print('-------------')
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t\t{mph:.1f}')