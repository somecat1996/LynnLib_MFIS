"""This file contains functions about prime. 
    IsPrime(x) is used to determine if x(an integer) is a prime. 
    ListPrimes(n) is used to list all primes less than n. n 
    should be greater than 0.
    FindPrimeAbove(x) is used to find the first prime greater 
    than x.
    FindPrimeBelow(x) is used to find the last prime less 
    than x.
    IsCoprime(a, b) determines whether a and b are coprime.
    MaximumCommonFactor(a, b) calculates the maximum common factor 
    between a and b.
    Bezout(a, b, s=False) calculates s and t which make s*a+t*b equals 
    to 1. Set s True to show how it process."""
from math import sqrt


def IsPrime(x):
    if not isinstance(x, int):
        raise TypeError("Input x should be an integer.")
    if x <= 1:
        return False
    else:
        prime_list = ListPrimes(int(sqrt(x)))
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


def IsCoprime(a, b):
    if MaximumCommonFactor(a, b) == 1:
        return True
    return False


def MaximumCommonFactor(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Input x should be an integer.")
    if a <= 0 or b <= 0:
        raise ValueError("a and b should be greater than 0.")
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        r1, r2 = r2, r1 % r2
    return r2

def Bezout(a, b, s=False):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Input x should be an integer.")
    if a <= 0 or b <= 0:
        raise ValueError("a and b should be greater than 0.")
    if not IsCoprime(a, b):
        raise ValueError("Cannot find the s, t that satisfies the condition.")
    q_array = []
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        q_array.append(r1 / r2)
        tmp = r1 % r2
        if s:
            print(str(r1)+'='+str(r1/r2)+'*'+str(r2)+'+'+str(tmp))
        r1 = r2
        r2 = tmp
    s_array = [1, 0]
    t_array = [0, 1]
    for i in q_array:
        s_array.append(-i * s_array[-1] + s_array[-2])
        t_array.append(-i * t_array[-1] + t_array[-2])
    if s:
        print('result: '+str(s_array[-1])+"*"+str(a)+"+"+str(t_array[-1])+"*"+str(b)+"="+str(r2))
    return s_array[-1], t_array[-1]


def Inverse():
    pass
