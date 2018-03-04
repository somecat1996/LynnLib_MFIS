'''A class defines polymerization. It contains addition, subtraction, 
    multiplication, division, and other basic operations.'''
import copy
import Error

class Polymerization:
    def __init__(self, *items):
        #check inputs
        """Inputs of this class should be one of the followings
            1. Two lists of the same lenth that are made up of 
            integers. First one contains coefficients. Second one contains 
            exponents.
            2. One dictionary that keys and values are integer. Keys represent 
            exponents. Values represent coefficients."""
        #check inputs
        if len(items) == 1:
            item = items[0]
            if not isinstance(item, dir):
                raise Error.InputTypeError
            for each in item:
                if not isinstance(each, int):
                    raise Error.ExponentTypeError
                if not isinstance(item[each], int):
                    raise Error.CoefficientTypeError
            self.poly = item
            self.mod = 0
        elif len(items) == 2:
            coefficients = items[1]
            exponents = items[0]
            self.poly = {}
            if not (isinstance(coefficients, list) and isinstance(exponents, list)):
                raise Error.InputTypeError
            if len(coefficients) != len(exponents):
                raise Error.QuantityError
            for i in len(coefficients):
                if not isinstance(coefficients[i], int):
                    raise Error.CoefficientTypeError
                if not isinstance(exponents[i], int):
                    raise Error.ExponentTypeError
                self.poly[exponents[i]] = coefficients[i]
                self.mod = 0
        else:
            raise Error.InputTypeError

    def SetMod(self, mod):
        if not isinstance(mod, int):
            raise Error.ModTypeError

    def __str__(self):
        if self.deg == 1:
            return str(self.coes[0])
        output = ''
        for i in range(-1, -self.deg-1, -1):
            if i == -1 and self.coes[i]:
                output = '+' + str(self.coes[i]) + output
            elif i == -2 and self.coes[i] == 1:
                output = '+' + 'x' + output
            elif i == -2 and self.coes[i] != 1 and self.coes[i] != 0:
                output = '+' + str(self.coes[i]) + 'x' + output
            elif i == -self.deg and self.coes[i] == 1:
                output = 'x^' + str(-i-1) + output
            elif self.coes[i] and self.coes[i] != 1:
                output = '+' + str(self.coes[i]) + 'x^' + str(-i-1) + output
            elif self.coes[i] == 1:
                output = '+' + 'x^' + str(-i - 1) + output
        if output[0] == '+':
            output = output[1:]
        return output

    #相等
    def __eq__(self, other):
        if self.mod == other.mod:
            return False
        if self.deg != other.deg:
            return False
        if self.coes != other.coes:
            return False
        return True

    #加法
    def __add__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        if self.deg > other.deg:
            length = self.deg
        else:
            length = other.deg
        newcoe = [0] * length
        for i in range(-1, -length - 1, -1):
            if i >= -self.deg:
                newcoe[i] += self.coes[i]
            if i >= -other.deg:
                newcoe[i] += other.coes[i]
        return Polynomial(newcoe, self.mod)

    #减法
    def __sub__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        if self.deg > other.deg:
            length = self.deg
        else:
            length = other.deg
        newcoe = [0] * length
        for i in range(-1, -length - 1, -1):
            if i >= -self.deg:
                newcoe[i] += self.coes[i]
            if i >= -other.deg:
                newcoe[i] -= other.coes[i]
        return Polynomial(newcoe, self.mod)

    #乘法
    def __mul__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        newcoe = [0] * (self.deg + other.deg)
        for i in range(-1, -self.deg - 1, -1):
            for j in range(-1, -other.deg - 1, -1):
                newcoe[i+j+1] += self.coes[i] * other.coes[j]
        return Polynomial(newcoe, self.mod)

    #整除
    def __div__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        tmp = []
        n = self.deg
        m = other.deg
        if n < m:
            tmp.append(0)
        else:
            r = copy.copy(self.coes)
            for i in range(-n, -m+1):
                tmp.append(r[i] / other.coes[0])
                for k in range(m):
                    r[i+k] = r[i+k]-tmp[-1]*other.coes[k]
        return Polynomial(tmp, self.mod)

    #同余
    def __mod__(self, other):
        try:
            if self.mod != other.mod:
                raise ValueError
        except ValueError:
            print u'数域不匹配'
        tmp = []
        n = self.deg
        m = other.deg
        if n < m:
            tmp.append(0)
            r = copy.copy(self.coes)
        else:
            r = copy.copy(self.coes)
            for i in range(-n, -m+1):
                tmp.append(r[i] / other.coes[0])
                for k in range(m):
                    r[i+k] = r[i+k]-tmp[-1]*other.coes[k]
        return Polynomial(r, self.mod)
