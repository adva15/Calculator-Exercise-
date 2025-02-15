import calculator

# דוגמאות לשאלות של המחשבון:
# a
def test_calculator_power():
# Arrange
    a: int = 2
    b: int = 2
    expected: int = 4
# Act
result = calculator.power(2, 2)
print(f"2 ** 2 = {result}")

# b
def test_calculator_sqrt():
# Arrange
    a: int = 9
    expected: int = 3
# Act

result = calculator.sqrt(9)
print(f"9 ** 0.5 = {result}")


# c
def test_factorial():
# Arrange
    a: int = 3
    expected: int = 6
 # Act
print(f'1*2*3=',calculator.factorial(3))


# תשובות לשאלות של הטסטים:
# d
def test_calculator_power2():
    # Arrange
    a: int = 2
    b: int = 4
    expected: int = 16

    # Act
    actual: int = calculator.power(a, b)
    assert expected == actual, "power numbers Completed"

result = calculator.power(2, 4)
print(f"2 ** 4 = {result}")


# e
def test_calculator_power3():
    # Arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    # Act
    actual: int = calculator.power(a, b)
    assert expected == actual, "power numbers Completed"

result = calculator.power(3, 2)
print(f"3 ** 2 = {result}")


# f
def test_calculator_sqrt2():
    # Arrange
    a: int = 25
    expected: int = 5

    # Act
    actual: int = calculator.sqrt(a)
    assert expected == actual, "sqrt numbers Completed"

result = calculator.sqrt(25)
print(f"25 ** 0.5 = {result}")


# g
import pytest

def test_calculator_error_sqrt():
    # Arrange
    a: int = -5

    # Act
    with pytest.raises(ValueError) as ex:
        calculator.make_error_sqrt(a)

# print(f'Error=',calculator.make_error_sqrt(-5))
# print(f'{result}')

# h
def test_factorial2():
  # Arrange
    num = 4
    expected: int = 24
    # Act
    actual: int = calculator.factorial(num)
    assert expected == actual, "factorial numbers Completed"
print(f'1*2*3*4=',calculator.factorial(4))

# i
# Act
print(f'1*2*3*4*5=', calculator.factorial(5))
print(f'{result}')

# j
# Arrange
num: int = -3

# Act
with pytest.raises(ValueError) as ex:
    calculator.factorial(-3)
# print(f'Error=', calculator.factorial(-3))
print(f'{result}')