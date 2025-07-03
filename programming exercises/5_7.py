CAT_A = 20
CAT_B = 15
CAT_C = 10

def get_cat():
    category_a = int(input('Сколько продано мест категории A: '))
    category_b = int(input('Сколько продано мест категории B: '))
    category_c = int(input('Сколько продано мест категории C: '))
    return category_a, category_b, category_c


def calculate(category_a, category_b, category_c):
    total = 0
    total += category_a * CAT_A
    total += category_b * CAT_B
    total += category_c * CAT_C
    return total


def main():
    cat_a, cat_b, cat_c = get_cat()
    total = calculate(cat_a, cat_b, cat_c)
    print(f'Доход от продажи билетов {total:,.2f}')


if __name__ == '__main__':
    main()