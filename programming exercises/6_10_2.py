def main():
    try:
        golf_file = open('golf.txt', 'r')
        name = golf_file.readline()
        while name:
            score = golf_file.readline()

            name = name.rstrip('\n')
            score = score.rstrip('\n')

            print(f'Игрок:{name}')
            print(f'Очков:{score}')

            name = golf_file.readline()

        golf_file.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
