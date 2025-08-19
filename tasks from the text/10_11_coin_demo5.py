# Эта программа импортирует имитационный модуль
# и создает три экземпляра класса Coin.

import coin_10_5

def main():
    # Создать три объекта класса Coin.
    cent = coin_10_5.Coin()
    gulden = coin_10_5.Coin()
    peso = coin_10_5.Coin()

    # Показать повернутую вверх сторону каждой монеты.
    print('Boт три монеты, у которых три стороны обращены вверх:')

    # Подбросить монету.
    print('Подбрасываю все три монеты ... ')
    print()
    cent.toss()
    gulden.toss()
    peso.toss()

    # Показать повернутую вверх сторону каждой монеты.
    print('Теперь обращены вверх вот эти стороны:')
    print(cent.get_sideup())
    print(gulden.get_sideup())
    print(peso.get_sideup())
    print()


if __name__ == '__main__':
    main()