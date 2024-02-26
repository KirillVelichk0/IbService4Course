import random
import math


def miller_rabin(number):
    """
    Реализация теста Миллера Рабина на простоту чисел
    :param number: число, которое проверяется на простоту тестом Миллера Рабина
    :return: булево значение, указывающее проходит число тест Миллера Рабина или нет
    """
    max_divisions_two = 0
    ec = number - 1
    while ec % 2 == 0:
        ec >>= 1
        max_divisions_two += 1
    assert 2**max_divisions_two * ec == number - 1

    def trial_composite(test: int):
        if pow(test, ec, number) == 1:
            return False
        for k in range(max_divisions_two):
            if pow(test, 2**k * ec, number) == number - 1:
                return False
        return True

    number_rabin_trials = 20
    for i in range(number_rabin_trials):
        round_tester = random.randrange(2, number)
        if trial_composite(round_tester):
            return False
    return True


def generate_prime_numbers(bit_size: int) -> int:
    """
    Функция возвращает простое число указанного размера бит
    :param bit_size: размер числа в битах
    :return: число заданного кол-ва бит
    """
    while True:
        number = random.getrandbits(bit_size)
        if not miller_rabin(number):
            continue
        else:
            return number


def find_coprime_number(number: int) -> int:
    """
    Функция нахождения взаимно простого числа
    :param number: число, для которого находим взаимно простое число
    :return: взаимно простое число числа number
    """
    bit_size = len(bin(number)[2:]) // 2
    start_number = random.getrandbits(bit_size)
    for i in range(start_number, number):
        if math.gcd(number, i) == 1:
            return i
    raise ValueError("Поиск взаимно простого числа не сработал")


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Расширенный алгоритм Евклида
    :return: возвращает НОД и два коэффициента x и y, такие что: ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def multiplicatively_inverse(e: int, fn: int) -> int:
    """
    Функция возвращает мультипликативно обратное число к числу e по модулю φ(n)
    """
    g, x, _ = egcd(e, fn)
    if g == 1:
        return x % fn
    raise ValueError("egcd не смог вернуть обратное")
