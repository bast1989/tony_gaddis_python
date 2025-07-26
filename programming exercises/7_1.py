DAYS = 7

def get_total_sales(sales_list):
    total = 0
    for s in sales_list:
        total += s

    return total


def main():
    sales_list = []

    for d in range(DAYS):
        value = float(input(f'Введите продажи за день {d + 1}: '))
        sales_list.append(value)

    total_sales = get_total_sales(sales_list)
    print(f'Сумма продаж за неделю: {total_sales:,.2f}')


if __name__ == '__main__':
    main()