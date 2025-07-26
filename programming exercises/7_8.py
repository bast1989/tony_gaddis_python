def main():
    boy_file = open('BoyNames.txt', 'r')
    boy_names = [i.rstrip('\n') for i in boy_file]
    boy_file.close()

    girl_file = open('GirlNames.txt', 'r')
    girl_names = [i.rstrip('\n') for i in girl_file]
    girl_file.close()

    search_name = input('Введите имя для проверки:')

    if search_name in boy_names and search_name in girl_names:
        print('Имя содержится в обоих списках.')
    elif search_name in boy_names:
        print('Имя содержится в списке мальчиков')
    elif search_name in girl_names:
        print('Имя содержится в списке девочек.')
    else:
        print('Имени нет в списках')

if __name__ == '__main__':
    main()