# A python program to create user-defined exception
# class MyError is derived from super class Exception


class InvalidDataTypeException(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

        # __str__ is to print() the value

    def __str__(self):
        return repr(self.value)


# A python program to create user-defined exception

# class MyError is derived from super class Exception
class DenominatorIsZero(Exception):

    # Constructor or Initializer
    def __init__(self, message):
        self.message = message

        # __str__ is to print() the value

    def __str__(self):
        return repr(self.message)


# A python program to create user-defined exception

# class MyError is derived from super class Exception
class DenominatorNegative(Exception):

    # Constructor or Initializer
    def __init__(self, message):
        self.message = message

        # __str__ is to print() the value

    def __str__(self):
        return repr(self.message)


# class MyError is derived from super class Exception
class IndexDataLengthNotMatching(Exception):

    # Constructor or Initializer
    def __init__(self, message):
        self.message = message

        # __str__ is to print() the value

    def __str__(self):
        return repr(self.message)


try:
    x = 5
    y = 2
    if y < 0:
        raise DenominatorNegative('Denominator can not be negative')
    z = x/y

# Value of Exception is stored in error
except ZeroDivisionError as error:
    raise DenominatorIsZero('Denominator can not be zero')