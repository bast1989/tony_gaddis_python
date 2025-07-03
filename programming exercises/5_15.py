def  calc_average(test_1, test_2, test_3, test_4, test_5):
    return (test_1 + test_2 + test_3 + test_4 + test_5) / 5

def determine_grade(test):
    if test >= 90:
        return 'Оценка А'
    elif test >= 80:
        return 'Оценка B'
    elif test >= 70:
        return 'Оценка C'
    elif test >= 60:
        return 'Оценка D'
    else:
        return 'Оценка F'

def main():
    test_1 = int(input('Введите оценку за тест 1: '))
    test_2 = int(input('Введите оценку за тест 2: '))
    test_3 = int(input('Введите оценку за тест 3: '))
    test_4 = int(input('Введите оценку за тест 4: '))
    test_5 = int(input('Введите оценку за тест 5: '))

    print(calc_average(test_1, test_2, test_3, test_4, test_5))
    print(determine_grade(test_1))
    print(determine_grade(test_2))
    print(determine_grade(test_3))
    print(determine_grade(test_4))
    print(determine_grade(test_5))

if __name__ == '__main__':
    main()