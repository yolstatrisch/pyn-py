"""
Pyn.py - A python library full of useless, mostly inefficient math functions that will make you say "Why?"

The ultimate goal of this library is to implement function that may or may not be needed to make complex functions like
Fourier Transform.
"""

__version__ = 0.3


def identity(number):
    """
    Identity function. Called by multiply_by_one and add_by_zero functions

    :returns the input:
    """
    return number


def add_by_zero(number):
    """
    Adds a number by zero

    :returns the input:
    """
    return identity(number)


def multiply_by_one(number):
    """
    Multiplies a number by one

    :returns the input:
    """
    return identity(number)


def multiply_int_by_zero(number):
    """
    Non-iterative implementation of multiplication of an integer by zero using bitwise operators

    :returns 0:
    """
    return number & ~number


def i_multiply_int_by_zero(number):
    """
    Iterative implementation of multiplication of an integer by zero using bitwise operators

    :returns 0:
    """
    while number & number:
        number = ~number >> 1

    return number


def bit_addition(bit_a, bit_b, carry_bit=False):
    """
    Binary bit addition with a carry bit

    Added in ver 0.2

    :returns a tuple of the form (return_bit, carry_bit):
    """
    return bit_a ^ bit_b ^ carry_bit, (bit_a & bit_b) ^ ((bit_a ^ bit_b) & carry_bit)


def f_abs(number):
    """
    This is how I get the absolute value of a number. Don't ask why

    :returns the absolute value of the number:
    """
    return (number ** 2) ** (1 / 2)


def negate(number):
    """
    A recursive implementation of the negate function

    :returns the negative of the input:
    """
    if f_abs(number) <= 1:
        return -number
    else:
        return 0 + negate(number / 2) * 2


def faster_sign(number):
    """
    A faster implementation of sign()

    Added in ver 0.2

    :returns the sign of the number (1, 0, -1):
    """
    try:
        return number / f_abs(number)
    except ZeroDivisionError:
        return 0


def sign(number):
    """
    A recursive implementation of the sign function

    :returns the sign of the number (1, 0, -1):
    """
    if (number ** 2) <= 1:
        if (number ** 2) ** (number ** 2) == 1:
            return number
        else:
            return number / f_abs(number)
    else:
        return sign(number // 2)
