"""This file contains functions about prime. 
    IsPrime(x) is used to determine if x(an integer) is a prime. 
    ListPrimes(n) is used to list all primes less than n. n 
    should be greater than 0.
    FindPrimeAbove(x) is used to find the first prime greater 
    than x.
    FindPrimeBelow(x) is used to find the last prime less 
    than x.
    IsCoprime(a, b) determines whether a and b are coprime.
    GetFactor(num, minimum=0) returns all prime factors of num that are 
    greator that minimum.
    CommonFactor(a, b) returns all common factors between a and b.
    MaximumCommonFactor(a, b) calculates the maximum common factor 
    between a and b.
    Bezout(a, b, s=False) calculates s and t which make s*a+t*b equals 
    to 1. Set s True to show how it process.
    Inverse(a, mod) calculates modulus m inverse of a.
    OnetimeCongruence(a, b, mod, s=False) returns sulotions of 
    ax=b (mod). Set s True to show how it process.
    CompleteSet(m) returns a list of complete set of m."""
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
    return MaximumCommonFactor(a, b) == 1


def GetFactor(num, minimum=0):
    array = list(range(2, num))
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            if array[j] % array[i] == 0:
                del array[j]
            else:
                j += 1
        i += 1
    j = 0
    while j < len(array):
        tmp = array[j]
        if minimum > tmp:
            del array[j]
        else:
            j += 1
    return array


def CommonFactor(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Input should be an integer.")
    if a <= 0 or b <= 0:
        raise ValueError("a and b should be greater than 0.")
    array = ListPrimes(int(sqrt(min(a, b))))
    i = 0
    while i < len(array):
        if a % array[i] == 0 and b % array[i] == 0:
            i += 1
        else:
            del array[i]
    return array


def MaximumCommonFactor(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Input should be an integer.")
    if a <= 0 or b <= 0:
        raise ValueError("a and b should be greater than 0.")
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        r1, r2 = r2, r1 % r2
    return r2


def Bezout(a, b, s=False):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Input should be an integer.")
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


def Inverse(a, mod):
    if not (isinstance(a, int) and isinstance(mod, int)):
        raise TypeError("Input should be an integer.")
    if a <= 0 or mod <= 0:
        raise ValueError("a and mod should be greater than 0.")
    if not IsCoprime(a, mod):
        raise ValueError("Cannot find the inverse of a.")
    s, t = Bezout(a, mod, False)
    return s


def OnetimeCongruence(a, b, mod, s=False):
    if not (isinstance(a, int) and isinstance(mod, int) and isinstance(b, int)):
        raise TypeError("Input should be an integer.")
    if a <= 0 or b <= 0 or mod <= 0:
        raise ValueError("a and mod should be greater than 0.")
    q_array = []
    r1 = a
    r2 = mod
    while r1 % r2 != 0:
        q_array.append(r1 / r2)
        tmp = r1 % r2
        r1 = r2
        r2 = tmp
    s_array = [1, 0]
    t_array = [0, 1]
    for i in q_array:
        s_array.append(-i * s_array[-1] + s_array[-2])
        t_array.append(-i * t_array[-1] + t_array[-2])
    if b % r2 != 0:
        if s:
            print("Congruence %dx=%d(mod %d) is unsolvable.") % (a, b, mod)
        return []
    else:
        if s:
            print("particular solution: x=%d y=%d") % (s_array[-1], t_array[-1])
            print("general solution: x=%d-t*%d y=%d+t*%d") % (s_array[-1], b/r2, t_array[-1], a/r2)
        return [(s_array[-1], b / r2), (t_array[-1], a / r2)]


def CompleteSet(m):
    if not isinstance(m, int):
        raise TypeError("Input should be an integer.")
    if m <= 0:
        raise ValueError("m should be greater than 0.")
    i = 0
    a = list(range(1, m))
    while i < len(a):
        r1 = a[i]
        r2 = m
        while r1 % r2 != 0:
            tmp = r1 % r2
            r1 = r2
            r2 = tmp
        if r2 == 1:
            i += 1
        else:
            del a[i]
    return a
