# Определение главной функции.
def main():
    get_name()
    print(f'Привет {name}.') #Эта инструкция вызовет ошибку!

# Определение функции get_name.
def get_name():
    name = input('Введите имя: ')

if __name__ == '__main__':
    main()