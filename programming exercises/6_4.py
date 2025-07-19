def main():
    i = 0
    try:
        nane_file = open('names.txt', 'r')
        for line in nane_file:
            i += 1
    except Exception as err:
        print(f'Ошибка: {err}')
    finally:
        nane_file.close()
        print(f'Имён в файле: {i}')


if __name__ == '__main__':
    main()