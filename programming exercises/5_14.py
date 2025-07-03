def kinetic_energy(mass, speed):
    return (1/2) * mass * (speed ** 2)

def main():
    mass = float(input('Введите массу в килограммах: '))
    speed = float(input('Введите скорость в метрах в секунду: '))
    print(f'Кинетическая энергия тела равна: {kinetic_energy(mass, speed)}')


if __name__ == '__main__':
    main()