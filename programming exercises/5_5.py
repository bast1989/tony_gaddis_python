COEFFICIENT_ESTIMATED_COST = 0.6
COEFFICIENT_DOLLAR = 0.0072



def get_estimated_cost():
    cost = float(input('Введите стоимость объекта: '))
    estimated_cost = cost * COEFFICIENT_ESTIMATED_COST
    return estimated_cost


def calculate_tax(estimated_cost):
    tax = estimated_cost * COEFFICIENT_DOLLAR
    return tax


def main():
    estimated_cost = get_estimated_cost()
    print(f'Налог равняется {calculate_tax(estimated_cost):,.2f}')


if __name__ == '__main__':
    main()