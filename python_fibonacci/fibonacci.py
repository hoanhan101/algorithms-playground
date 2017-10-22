#!/usr/bin/env python3

"""
	fibonacci.py - Fibonacci's implementation in 3 different ways
	Author: Hoanh An (hoanhan@bennington.edu)
	Date: 10/18/2017
"""

import time


# Fibonacci Naive Recursion
def fib_naive_recursion(n):
    if n <= 2:
         return 1
    else:
        return fib_naive_recursion(n - 1) + fib_naive_recursion(n - 2)

# Fibonacci Memoized DP Algorithm
memo = {}
def fib_memoized_dp(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib_memoized_dp(n - 1) + fib_memoized_dp(n - 2)
    memo[n] = result

    return result

# Fibonacci Bottom-up DP Algorithm
def fib_bottom_up_dp(n):
    fib = {}
    for k in range(n+1):
        if k <= 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f

    return fib[n]

if __name__ == '__main__':
    """
        Let n = 35.
        Calculate the time it takes foe each function to execute
    """
    n = 35
    start_time = time.time()
    fib_naive_recursion(n)
    end_time = time.time() - start_time
    print("Fibonacci Naive Recursion: {0}".format(end_time))

    start_time = time.time()
    fib_memoized_dp(n)
    end_time = time.time() - start_time
    print("Fibonacci Memoized DP Algorithm: {0}".format(end_time))

    start_time = time.time()
    fib_bottom_up_dp(n)
    end_time = time.time() - start_time
    print("Fibonacci Bottom-up DP Algorithm: {0}".format(end_time))



