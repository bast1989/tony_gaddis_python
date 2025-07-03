G = 9.8

def falling_distance(sec):
    return (1/2) * G * (sec ** 2)

def main():
    print(f'|{'Время в с секундах':^20}|{'Расстояние в метрах':^25}|')
    print('------------------------------------------------')
    for sec in range(1, 11):
        print(f'|{sec:^20}|{falling_distance(sec):^25.2f}|')
        print('------------------------------------------------')



if __name__ == '__main__':
    main()