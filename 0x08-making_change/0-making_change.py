#!/usr/bin/python3
"""
Module to determine the minimum number of coins needed to meet a given amount.
"""

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total amount.
    
    Args:
    coins (list): List of coin denominations.
    total (int): The total amount we need to make.
    
    Returns:
    int: The minimum number of coins needed to make the total amount,
         or -1 if it's not possible to make the total amount with given coins.
    """
    if total <= 0:
        return 0

    # Initialize DP array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
