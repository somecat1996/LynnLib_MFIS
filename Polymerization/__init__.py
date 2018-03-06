'''A class defines polymerization. It contains addition, subtraction, 
    multiplication, division, and other basic operations.'''
import copy
import Error
import Prime

class Polymerization:
    def __init__(self, *items):
        #check inputs
        """Inputs of this class should be one of the followings:
            1. Two lists of the same lenth that are made up of 
            integers. First one contains coefficients. Second one contains 
            exponents.
            2. One dictionary that keys and values are integer. Keys represent 
            exponents. Values represent coefficients.
            
            self.coefficients is a list contains coefficients of polymerization.
            self.mod is an integer represents coefficients' generator. It 
            should be a prime. User can use SetMod(mod) to set this value. 
            Zero represent natural number.
            self.degree is an integer represents the exponent of the largest item."""
        #check inputs
        if len(items) == 1:
            item = copy.deepcopy(items[0])
            if isinstance(item, dict):
                for each in item:
                    if not isinstance(each, int):
                        raise Error.ExponentTypeError
                    if not isinstance(item[each], int):
                        raise Error.CoefficientTypeError
                tmp = list(item.keys())
                tmp.sort(reverse=True)
                deg = tmp[0]
                self.coefficients = [0] * (deg + 1)
                for i in range(deg + 1):
                    try:
                        self.coefficients[-i-1] = item[i]
                    except:
                        self.coefficients[-i-1] = 0
                self.mod = 0
                self.degree = deg
            elif isinstance(item, list):
                for each in item:
                    if not isinstance(each, int):
                        raise Error.CoefficientTypeError
                while item[0] == 0 and len(item) > 1:
                    del item[0]
                self.coefficients = copy.deepcopy(item)
                self.mod = 0
                self.degree = len(item) - 1
            else:
                raise Error.InputTypeError
        elif len(items) == 2:
            coefficients = copy.deepcopy(items[1])
            exponents = copy.deepcopy(items[0])
            if not (isinstance(coefficients, list) and isinstance(exponents, list)):
                raise Error.InputTypeError
            if len(coefficients) != len(exponents):
                raise Error.QuantityError
            try:
                deg = max(exponents)
            except:
                deg = 0
            self.coefficients = [0] * (deg + 1)
            for i in range(deg + 1):
                try:
                    self.coefficients[-i - 1] = coefficients[exponents.index(i)]
                except:
                    self.coefficients[-i - 1] = 0
            self.mod = 0
            self.degree = deg
        else:
            raise Error.InputTypeError

    def SetMod(self, mod):
        # Set self.mod
        # self.mod should be a prime
        if not isinstance(mod, int):
            raise Error.ModTypeError
        if (not Prime.IsPrime(mod)) and mod != 0:
            raise Error.ModValueError
        self.mod = mod
        self._Mod()

    def _Mod(self):
        if self.mod > 0:
            for each in range(self.degree+1):
                self.coefficients[each] = self.coefficients[each] % self.mod
            while self.coefficients[0] == 0 and len(self.coefficients) > 1:
                del self.coefficients[0]
                self.degree -= 1

    def __str__(self):
        # convert to string
        output = ''
        if self.degree == 0:
            return str(self.coefficients[0]) + '\ndegree:0'
        for each in range(-self.degree-1, 0):
            if each == -1:
                if self.coefficients[each] < 0:
                    output += str(self.coefficients[each])
                elif self.coefficients[each] != 0:
                    output += '+' + str(self.coefficients[each])
            elif each == -2:
                if self.coefficients[each] < 0:
                    if self.coefficients[each] == -1:
                        output += '-x'
                    else:
                        output += str(self.coefficients[each]) + 'x'
                elif self.coefficients[each] == 1:
                    output += '+' + 'x'
                elif self.coefficients[each] != 0:
                    output += '+' + str(self.coefficients[each]) + 'x'
            else:
                if self.coefficients[each] < 0:
                    if self.coefficients[each] == -1:
                        output += '-x^' + str(-each-1)
                    else:
                        output += str(self.coefficients[each]) + 'x^' + str(-each-1)
                elif self.coefficients[each] == 1:
                    output += '+' + 'x^' + str(-each-1)
                elif self.coefficients[each] != 0:
                    output += '+' + str(self.coefficients[each]) + 'x^' + str(-each-1)
        return output[1:] + '\ndegree: ' + str(self.degree)

    def __eq__(self, other):
        #equation
        if self.mod != other.mod:
            return False
        if self.degree != other.degree:
            return False
        if self.coefficients != other.coefficients:
            return False
        return True

    def __add__(self, other):
        # addition
        if self.mod != other.mod:
                raise Error.CalculateModError
        if self.degree > other.degree:
            length = self.degre + 1
        else:
            length = other.degree + 1
        newcoe = [0] * length
        for i in range(length):
            if i <= self.degree:
                newcoe[i] += self.coefficients[i]
            if i <= other.degree:
                newcoe[i] += other.coefficients[i]
        output = Polymerization(newcoe)
        output.SetMod(self.mod)
        return output

    def __sub__(self, other):
        # substraction
        if self.mod != other.mod:
            raise Error.CalculateModError
        if self.degree > other.degree:
            length = self.degree + 1
        else:
            length = other.degree + 1
        newcoe = [0] * length
        for i in range(length):
            if i <= self.degree:
                newcoe[i] += self.coefficients[i]
            if i <= other.degree:
                newcoe[i] -= other.coefficients[i]
        output = Polymerization(newcoe)
        output.SetMod(self.mod)
        return output

    def __mul__(self, other):
        # multiplication
        if self.mod != other.mod:
            raise Error.CalculateModError
        newcoe = [0] * (self.degree + other.degree + 1)
        for i in range(-1, -self.degree - 1, -1):
            for j in range(-1, -other.degree - 1, -1):
                newcoe[i+j+1] += self.coefficients[i] * other.coefficients[j]
        output = Polymerization(newcoe)
        output.SetMod(self.mod)
        return output

    def __divmod__(self, other):
        return self / other, self % other

    def __truediv__(self, other):
        # division
        if self.mod != other.mod:
            raise Error.CalculateModError
        tmp = []
        n = self.degree
        m = other.degree
        if n < m:
            tmp.append(0)
        else:
            r = copy.copy(self.coefficients)
            for i in range(-n-1, -m):
                tmp.append(int(r[i] / other.coefficients[0]))
                for k in range(m):
                    r[i+k] = r[i+k]-tmp[-1]*other.coefficients[k]
        output = Polymerization(tmp)
        output.SetMod(self.mod)
        return output

    def __mod__(self, other):
        # congruence
        if self.mod != other.mod:
            raise Error.CalculateModError
        tmp = []
        n = self.degree
        m = other.degree
        if n < m:
            tmp.append(0)
            r = copy.copy(self.coefficients)
        else:
            r = copy.copy(self.coefficients)
            for i in range(-n-1, -m):
                tmp.append(int(r[i] / other.coefficients[0]))
                for k in range(m):
                    r[i+k] = r[i+k]-tmp[-1]*other.coefficients[k]
        output = Polymerization(r)
        output.SetMod(self.mod)
        return output

    def __len__(self):
        return self.degree

    def __or__(self, other):
        if self.mod != 2 and self.mod != 2:
            raise Error.LogicalOperationError
        if self.degree > other.degree:
            length = self.degre + 1
        else:
            length = other.degree + 1
        newcoe = [0] * length
        for i in range(length):
            if i <= self.degree:
                newcoe[i] += self.coefficients[i]
            if i <= other.degree:
                newcoe[i] += other.coefficients[i]
        for i in range(length):
            if newcoe[i] > 0:
                newcoe[i] = 1
        output = Polymerization(newcoe)
        output.SetMod(self.mod)
        return output


    def __and__(self, other):
        if self.mod != 2 and self.mod != 2:
            raise Error.LogicalOperationError
        if self.degree > other.degree:
            length = self.degre + 1
        else:
            length = other.degree + 1
        newcoe = [0] * length
        for i in range(length):
            if i <= self.degree:
                newcoe[i] += self.coefficients[i]
            if i <= other.degree:
                newcoe[i] += other.coefficients[i]
        for i in range(length):
            if newcoe[i] == 2:
                newcoe[i] = 1
            else:
                newcoe[i] = 0
        output = Polymerization(newcoe)
        output.SetMod(self.mod)
        return output

    def __xor__(self, other):
        if self.mod != 2 and self.mod != 2:
            raise Error.LogicalOperationError
        if self.degree > other.degree:
            length = self.degre + 1
        else:
            length = other.degree + 1
        newcoe = [0] * length
        for i in range(length):
            if i <= self.degree:
                newcoe[i] += self.coefficients[i]
            if i <= other.degree:
                newcoe[i] += other.coefficients[i]
        for i in range(length):
            if newcoe[i] == 2:
                newcoe[i] = 0
        output = Polymerization(newcoe)
        output.SetMod(self.mod)
        return output

    def __lt__(self, other):
        raise Error.CompareError

    def __gt__(self, other):
        raise Error.CompareError

    def __le__(self, other):
        raise Error.CompareError

    def __ge__(self, other):
        raise Error.CompareError
