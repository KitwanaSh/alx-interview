#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """
    The minimun operation task
    Desc:
        paramemter: n
        return: Intersection
    """
    if n <= 1:
        return 0
    for operation in range(2, n+1):
        if n % operation == 0:
            return minOperations(int(n/operation)) + operation
