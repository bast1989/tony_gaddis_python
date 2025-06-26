# Эта программ демонстрирует две функции, которые
# имеют локальные переменные с одинаковыми именами.

def main():
    # Вызвать функцию texas.
    texas()
    # Вызвать функцию california.
    california()

def texas():
    birds = 5000
    print(f'В Техасе обитает {birds} птиц.')

def california():
    birds = 8000
    print(f'В Калифорнии обитает {birds} птиц.')

if __name__ == '__main__':
    main()