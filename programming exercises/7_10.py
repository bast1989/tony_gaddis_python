def main():
    winners_total = 0

    winners_file = open('WorldSeriesWinners.txt', 'r')
    winners_list = [i.rstrip('\n') for i in winners_file]
    winners_file.close()
    winners_set = set(winners_list)

    print('Список команд-победителей Мировой серии по бейсболу с 1903 по 2009 год: ')
    for i in winners_set:
        print(i)

    search_winners = input('Введите название команды для подсчёта количества побед: ')

    for i in winners_list:
        if i == search_winners:
            winners_total += 1

    print(f'Команда: {search_winners} победила раз: {winners_total}.')


if __name__ == '__main__':
    main()