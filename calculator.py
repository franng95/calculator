import math


def adittion(a, b):
        """Return the sum of a and b.

        Kept the original (misspelled) function name to avoid
        breaking callers that may already depend on it.
        """
        return a + b

def subtraction(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b

def multiplication(a, b):
    """Return the product of a and b."""
    return a * b

def division(a, b):
    """Return a divided by b.

    Raises ValueError when attempting to divide by zero.
    """
    if b == 0:
        # Defensive check: division by zero is undefined.
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """Return a raised to the power of b (a ** b)."""
    return a ** b

def square_root(a):
    """Return the square root of a.

    Raises ValueError for negative inputs since the real-valued
    square root is undefined for negatives.
    """
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    # Use exponent 0.5 rather than math.sqrt to keep behavior simple.
    return a ** 0.5

def modulus(a, b):
    """Return the modulus (remainder) of a divided by b (a % b)."""
    return a % b

def floor_division(a, b):
    """Return the floor division result of a // b.

    Raises ValueError when dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b

def logarithm(a, base=10):
    """Return the logarithm of a with given base (default base 10).

    Raises ValueError for non-positive `a` since log is undefined there.
    """
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)

def sine(angle_rad):
    """Return the sine of an angle given in radians."""
    return math.sin(angle_rad)

def cosine(angle_rad):
    """Return the cosine of an angle given in radians."""
    return math.cos(angle_rad)

def tangent(angle_rad):
    """Return the tangent of an angle given in radians."""
    return math.tan(angle_rad)

def factorial(n):
    """Return the factorial of n.

    Raises ValueError for negative inputs since factorial is
    undefined for negative integers.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def exponential(a):
    """Return e raised to the power of a (the exponential function)."""
    return math.exp(a)

def absolute(a):
    """Return the absolute value of a."""
    return abs(a)

def round_number(a):
    """Round a to the nearest integer using Python's built-in round()."""
    return round(a)

def max_of_two(a, b):
    """Return the larger of the two values a and b."""
    return max(a, b)

def min_of_two(a, b):
    """Return the smaller of the two values a and b."""
    return min(a, b)

def average(numbers):
    """Return the arithmetic mean of a sequence of numbers.

    Raises ValueError if `numbers` is empty or falsy to avoid
    a division-by-zero situation.
    """
    if not numbers:
        raise ValueError("Cannot compute the average of an empty list.")
    return sum(numbers) / len(numbers)