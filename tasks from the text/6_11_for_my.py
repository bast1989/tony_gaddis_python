def main():
    iteration = int(input('Введите количество роликов: '))
    length_file = open('length_of_the_roller.txt', 'w')
    for i in range(iteration):
        length_roll = input(f'Введите длину ролика {i + 1}: ')
        length_file.write(f'{length_roll}\n')
    length_file.close()

if __name__ == '__main__':
    main()