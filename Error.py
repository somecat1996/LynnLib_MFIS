"""This file contains error classes used in other files."""


class CoefficientTypeError(TypeError):
    def __init__(self):
        TypeError.__init__(self, "Coefficients should be integers.")


class ExponentTypeError(TypeError):
    def __init__(self):
        TypeError.__init__(self, "Exponents should be integers.")


class QuantityError(ValueError):
    def __init__(self):
        ValueError.__init__(self, "The number of coefficients and exponents should be the same.")


class InputTypeError(TypeError):
    def __init__(self):
        TypeError.__init__(self, "Inputs doesn't match any of the followings:\n\t1. Two " +
                                 "lists of the same lenth that are made up of " +
                                 "integers. First one contains coefficients. Second one " +
                                 "contains exponents.\n\t" +
                                 "2. One dictionary that keys and values are integer. Keys " +
                                 "represent exponents. Values represent coefficients.")


class ModTypeError(TypeError):
    def __init__(self):
        TypeError.__init__(self, "Generator should be an integer.")
