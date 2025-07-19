def main():
    players = int(input('Сколько игроков на поле? '))
    try:
        players_file = open('golf.txt', 'w')
        for i in range(players):
            name = input('Введите имя игрока: ')
            score = input('Введите его счёт: ')
            players_file.write(f'{name}\n')
            players_file.write(f'{score}\n')
        players_file.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()