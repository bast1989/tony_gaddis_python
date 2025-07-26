def main():
    population_file = open('USPopulation.txt', 'r')
    population_list = [int(i) for i in population_file]
    population_file.close()
    total = 0

    for i in population_list:
        total += i

    print(f'{total / len(population_list):.2f}')
    print(f'{min(population_list)}')
    print(f'{max(population_list)}')


if __name__ == '__main__':
    main()