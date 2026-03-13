#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a non-negative integer using recursion.
        The factorial of a number n is the product of all positive integers
        less than or equal to n.

    Parameters:
        n (int): A non-negative integer whose factorial will be calculated.

    Returns:
        int: The factorial value of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Get the number from command line arguments
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)