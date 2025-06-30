CAR_EXPENSES = (
            'платеж по кредиту',
            'страховка',
            'бензин',
            'машинное масло',
            'шины',
            'техобслуживание'
)
YEAR = 12


def get_expenses():
      print('Программа выведет категории расходов на авто.')
      print('Введите среднюю стоимость категории в месяц.')
      expenses = {}
      for i in CAR_EXPENSES:
          cost = float(input(f'Введите стоимость категории {i} в месяц: '))
          expenses[i] = cost
      return expenses


def cost_calculation(expenses):
      expenses_month = 0
      for k, v in expenses.items():
            expenses_month += v
      expenses_year = expenses_month * YEAR
      return expenses_month, expenses_year


def main():
      dic = get_expenses()
      month, year = cost_calculation(dic)
      print(f'Расходы за месяц составили: {month}',
            f'Расходы за год составили: {year}', sep='\n')


if __name__ == '__main__':
    main()
