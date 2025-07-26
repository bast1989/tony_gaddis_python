# Эта программа применяет метод writelines дпя сохранения
# списка строковых значений в файл.

def main():
    # Создать список строковых значений.
    cities = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']

    # Открыть файл дпя записи.
    out_file = open('cities.txt', 'w', encoding='utf-8')

    # Записать список в файл.
    out_file.writelines(cities)

    # Закрыть файл.
    out_file.close()


if __name__ == '__main__':
    main()
