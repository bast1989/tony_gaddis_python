COEFFICIENT = 0.8

def get_cost():
      cost = float(input('Введите стоимость недвижимости: '))
      return cost


def insurance_calculation(cost):
      insurance = cost * COEFFICIENT
      return insurance


def main():
      cost = get_cost()
      insurance = insurance_calculation(cost)
      print(f'Средня стоимость страховки от ${cost:,.2f} составляет ${insurance:,.2f}')


if __name__ == '__main__':
    main()