"""This file contains functions about prime. 
    IsPrime(x) is used to determine if x(an integer) is a prime. 
    ListPrimes(n) is used to list all primes less than n. n 
    should be greater than 0.
    FindPrimeAbove(x) is used to find the first prime greater 
    than x.
    FindPrimeBelow(x) is used to find the last prime less 
    than x."""
from math import sqrt


def IsPrime(x):
    if not isinstance(x, int):
        raise TypeError("Input x should be an integer.")
    if x <= 1:
        return False
    else:
        prime_list = ListPrimes(sqrt(x))
        for each in prime_list:
            if x % each == 0:
                return False
        return True


def ListPrimes(n):
    if not isinstance(n, int):
        raise TypeError("Input n should be an integer.")
    output = []
    i = 1
    while i < n:
        is_deleted = False
        i = i + 1
        for each in output:
            if i % each == 0:
                is_deleted = True
        if not is_deleted:
            output.append(i)
    return output


def FindPrimeAbove(x):
    if not isinstance(x, int):
        raise TypeError("Input x should be an integer.")
    tmp = False
    while not tmp:
        x = x + 1
        tmp = IsPrime(x)
    return x


def FindPrimeBelow(x):
    if not isinstance(x, int):
        raise TypeError("Input x should be an integer.")
    tmp = False
    while not tmp:
        if x <= 1:
            raise ValueError("Prime less than x is not exist.")
        x = x - 1
        tmp = IsPrime(x)
    return x
