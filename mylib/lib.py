# lib.py

def multiply(x: int, y: int) -> int:
    """
    Multiplies two numbers and returns the result.
    
    :param x: First number
    :param y: Second number
    :return: Product of x and y
    """
    return x * y


def add_then_multiply(x: int, y: int) -> int:
    """
    Adds two numbers and multiplies the result by 2.
    
    :param x: First number
    :param y: Second number
    :return: (x + y) * 2
    """
    sum_result = x + y
    return sum_result * 2


def calculate_average(x: int, y: int) -> float:
    """
    Calculates the average of two numbers.
    
    :param x: First number
    :param y: Second number
    :return: Average of x and y
    """
    sum_result = x + y
    return sum_result / 2
