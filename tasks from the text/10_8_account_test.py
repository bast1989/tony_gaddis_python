# Эта программа демонстрирует класс BankAccount.

import bankaccount_10_7

def main():
    # Получить начальньм остаток.
    start_bal = float(input('Bвeдитe свой начальный остаток : '))

    # Получить начальный остаток.
    savings = bankaccount_10_7.BankAccount(start_bal)

    # Внести на счёт зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе?: '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    # Показать остаток.
    print(f'Baш остаток на счете составляет ${savings.get_balance():,.2f}')

    # Получить сумму для снятия с банковского счета.
    cash = float(input('Kaкyю сумму Вы желаете снять со счета?: '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    # Показать остаток.
    print(f'Baш остаток на счете составляет ${savings.get_balance():,.2f}')


if __name__ == '__main__':
    main()