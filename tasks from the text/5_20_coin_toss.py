# Эта программа имитирует 10 бросков монеты
import random

# Константы.
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for count in range(TOSSES):
        # Имитировать бросание монеты.
        coin = random.randint(HEADS, TAILS)
        if coin == HEADS:
            print('Монетка упала орлом вверх.')
        else:
            print('Монетка упала решкой вверх.')

if __name__ == '__main__':
    main()