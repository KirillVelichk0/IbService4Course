from prime_numbers import (
    generate_prime_numbers,
    find_coprime_number,
    multiplicatively_inverse,
)


class Rsa:
    def __init__(self, bit_size: int):
        self.bit_size = bit_size
        self.__p = generate_prime_numbers(bit_size)
        self.__q = generate_prime_numbers(bit_size)
        self.__n = self.__p * self.__q
        self.__phi = (self.__p - 1) * (self.__q - 1)
        self.__e = find_coprime_number(self.__phi)
        self.__d = multiplicatively_inverse(self.__e, self.__phi)

    @property
    def public_key(self) -> tuple[int, int]:
        return self.__e, self.__n

    @property
    def private_key(self) -> tuple[int, int]:
        return self.__d, self.__n

    @property
    def all_parameters(self) -> tuple[int, int, int, int, int, int]:
        return self.__p, self.__q, self.__n, self.__phi, self.__e, self.__d
