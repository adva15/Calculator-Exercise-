import math
import sqlite3

def add(a, b):
    return a + b  # + 0.1 # 0.99999999999

def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

# a
def power(a, b):
    return a ** b

# b
def sqrt(a):
    return a ** 0.5

# c
def factorial(num):
    if num < 0:
     raise ValueError()
    else:
        result = 1
        for i in range(1, num + 1, 1):
            result *= i
        return result

# g
def make_error_sqrt(a):
    raise ValueError()



