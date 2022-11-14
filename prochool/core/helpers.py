from random import randrange
from functools import reduce

from django.db.models import Model


def generate(length: int = 12) -> list:
    '''Generate n (length) random number from 2 -> 9'''
    numbers = []
    for n in range(length):
        numbers.append(randrange(2, 10))
    return numbers


def checksum(numbers: list) -> int:
    '''EAN 13 checksum'''

    def sum(x, y): return int(x) + int(y)
    evensum = reduce(sum, numbers[::2])
    oddsum = reduce(sum, numbers[1::2])

    return (10 - ((evensum + oddsum * 3) % 10)) % 10


def generate_ean_13():
    digits = generate()
    digits.append(checksum(digits))
    return ''.join(map(str, digits))


def generate_unique_code(model: Model) -> str:
    '''Generate unique for model

    continue generate codes untill get a unique one
    '''
    while True:
        code = generate_ean_13()
        try:
            model.objects.get(barre_code=code)
        except model.DoesNotExist:
            return code
