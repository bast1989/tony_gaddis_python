# Эта программа вычисляет заработную плату
# для каждого сотрудника Меган.

# NUM_EMPLOYEES применяется как константа
# для размера списка.
NUM_EMPLOYEES = 6

def main():
    # Создать список, который будет содержать отработанные часы.
    hours = [0] * NUM_EMPLOYEES

    # Получить часы, отработанные каждым сотрудником.
    for i in range(NUM_EMPLOYEES):
        salary = int(input(f'Введите количество часов сотрудника {i + 1}: '))
        hours[i] = salary

    # Получить почасовую ставку оплаты.
    pay_rate = float(input(f'Введите часовую ставку: '))

    # Показать заработную плату каждого сотрудника.
    for i in range(NUM_EMPLOYEES):
        gross_pay = hours[i] * pay_rate
        print(f'Зарплата сотрудника {i + 1} составила: ${gross_pay:,.2f}')


if __name__ == '__main__':
    main()