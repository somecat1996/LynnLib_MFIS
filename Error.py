"""This file contains error classes used in other files."""


class CoefficientTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Coefficients should be integers.")


class ExponentTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Exponents should be integers.")


class RepeatedExponentError(Exception):
    def __init__(self):
        Exception.__init__(self, "You input two or more repeated exponents.")


class QuantityError(Exception):
    def __init__(self):
        Exception.__init__(self, "The number of coefficients and exponents should be the same.")


class InputTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Inputs doesn't match any of the followings:\n\t1. Two " +
                                 "lists of the same lenth that are made up of " +
                                 "integers. First one contains coefficients. Second one " +
                                 "contains exponents.\n\t" +
                                 "2. One dictionary that keys and values are integer. Keys " +
                                 "represent exponents. Values represent coefficients.")


class ModTypeError(Exception):
    def __init__(self):
        Exception.__init__(self, "Generator should be an integer.")


class ModValueError(Exception):
    def __init__(self):
        Exception.__init__(self, "Generator should be a prime.")


class CalculateModError(Exception):
    def __init__(self):
        Exception.__init__(self, "Polynomials with different generators cannot be calculated")


class LogicalOperationError(Exception):
    def __init__(self):
        Exception.__init__(self, "Only 0/1 domains can perform logical operations.")


class CompareError(Exception):
    def __init__(self):
        Exception.__init__(self, "Can't compare two polymerizations.")
