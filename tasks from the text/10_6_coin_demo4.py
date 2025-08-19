# Эта программа импортирует модуль coin
# и создает экземпляр класса Coin.

import coin_10_5

def main():
    # Создать объект на основе класса Coin.
    cent = coin_10_5.Coin()

    # Показать обращенную вверх сторону монеты.
    print(f'Этa сторона обращена вверх: {cent.get_sideup()}')

    print('Собираюсь подбросить монету десять раз:')
    for i in range(10):
        cent.toss()
        print(cent.get_sideup())


if __name__ == '__main__':
    main()