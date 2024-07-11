#!/usr/bin/python3
"""
Module to calculate the minimum number of operations to get `n` characters.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n `H` characters in the file.
    
    Args:
    n (int): The number of characters desired
    
    Returns:
    int: The minimum number of operations needed to get `n` characters, or 0 if impossible
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

