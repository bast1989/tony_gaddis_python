def get_the_data():
    fats = int(input('Введите количество жиров: '))
    carbohydrates = int(input('Введите количество углеводов: '))
    return fats, carbohydrates


def calculate_calories(fats, carbohydrates):
    calories_in_fats = fats * 9
    calories_in_carbohydrates = carbohydrates * 4
    all_calories = calories_in_fats + calories_in_carbohydrates
    return calories_in_fats, calories_in_carbohydrates, all_calories


def main():
    fats, carbohydrates = get_the_data()
    calories_in_fats, calories_in_carbohydrates, all_calories = calculate_calories(fats, carbohydrates)
    print(f'Калорий от жиров {calories_in_fats}',
          f'Калорий от углеводов {calories_in_carbohydrates}',
          f'Калорий всего {all_calories}', sep='\n')


if __name__ == '__main__':
    main()
