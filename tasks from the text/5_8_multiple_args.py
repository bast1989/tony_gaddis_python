# Эта программа демонстрирует функцию, которая принимает
# два аргумента.


def main():
    print('Сумма чисел 12 и 45 равняется')
    show_sum(12, 45)

    
def show_sum(num1, num2):
    result = num1 + num2
    print(result)


if __name__ == '__main__':
    main()