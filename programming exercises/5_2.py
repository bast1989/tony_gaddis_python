def get_pay():
      amount_bay = float(input('Введите сумму покупки: '))
      return amount_bay

def calculate_fed_tax(pay):
      fed_tax = pay * 0.05
      return fed_tax


def calculate_reg_tax(pay):
      reg_tax = pay * 0.025
      return reg_tax


def main():
      amount_bay = get_pay()
      fed_tax = calculate_fed_tax(amount_bay)
      reg_tax = calculate_reg_tax(amount_bay)
      print(f'Сумма покупки равна: {amount_bay:,.2f}',
            f'Федеральный налог составил: {fed_tax:,.2f}',
            f'Региональный налог составил: {reg_tax:,.2f}',
            f'Общий налог с продаж составил: {fed_tax + reg_tax:,.2f}',
            f'Сумма к оплате: {amount_bay + fed_tax + reg_tax:,.2f}', sep='\n')


if __name__ == '__main__':
    main()