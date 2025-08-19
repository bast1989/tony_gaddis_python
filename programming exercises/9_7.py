def main():
    number_of_wins = dict()
    wins = 0
    not_play = [1904, 1994]
    table_of_wins = dict()

    with open('WorldSeriesWinners.txt', 'r') as win_file:
        winners = win_file.read()

    winners_list = winners.split('\n')
    unique_winners = set(winners_list)

    for u_win in unique_winners:
        for l_win in winners_list:
            if u_win == l_win:
                wins += 1
        number_of_wins[u_win] = wins
        wins = 0

    years_play = [i for i in range(1903, 2009) if i not in not_play]

    for i in range(len(years_play)):
        table_of_wins[years_play[i]] = winners_list[i]

    year = int(input('Введите год: '))

    print(f'В это году победила команда {table_of_wins.get(year, "Такой год не найден.")}, она побеждала {number_of_wins.get(table_of_wins[year], "Команда не найдена")} раз')






if __name__ == '__main__':
    main()
