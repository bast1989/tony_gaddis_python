import random

def cast_converter(cast):
    if cast == 1:
        return 'камень'
    elif cast == 2:
        return 'ножницы'
    else:
        return 'бумага'


def result(ai_cast, player_cast):
    if ai_cast == 'камень' and player_cast == 'ножницы':
        print('Камень разбивает ножницы - победил компьютер.')
    elif ai_cast == 'ножницы' and player_cast == 'камень':
        print('Камень разбивает ножницы - победил игрок.')
    elif ai_cast == 'ножницы' and player_cast == 'бумага':
        print('Ножницы режут бумагу - победил компьютер.')
    elif ai_cast == 'бумага' and player_cast == 'ножницы':
        print('Ножницы режут бумагу - победил игрок.')
    elif ai_cast == 'бумага' and player_cast == 'камень':
        print('Бумага заворачивает камень - победил компьютер.')
    elif ai_cast == 'камень' and player_cast == 'бумага':
        print('Бумага заворачивает камень - победил игрок.')
    else:
        print('Оба игрока сделали одинаковый выбор,для определения победителя нужно сыграть повторный раунд.')


def main():
    ai_cast = 0
    player_cast = 0
    while ai_cast == player_cast:
        ai_cast = cast_converter(random.randint(1, 3))
        player_cast = cast_converter(int(input('Введите: 1 если камень, 2 если ножницы или 3 если бумага: ')))
        result(ai_cast, player_cast)


if __name__ == '__main__':
    main()
