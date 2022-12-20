from math import sqrt

message: str = 'Добро пожаловать в самую лучшую программу для вычисления '
message += 'квадратного корня из заданного числа. '


def calculatesquareroot(number) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number) -> float:
    if your_number <= 0:
        return "Невозможно вычислить корень"
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {calculatesquareroot(your_number)}')


print(message)
calc(25.5)
