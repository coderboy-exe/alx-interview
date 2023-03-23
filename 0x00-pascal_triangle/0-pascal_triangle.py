#!/usr/bin/python3
""" Returns a list of integers representing pascal's triangle of n"""


def pascal_triangle(n):
    """Generates pascal's triangle for a given input value(number)"""

    if n <= 0:
        return []

    triangle = [1]
    result = [triangle]

    for i in range(n-1):
        row = []
        row.append(triangle[0])
        for i in range(len(triangle) - 1):
            row.append(triangle[i] + triangle[i + 1])
        row.append(triangle[-1])
        triangle = row
        result.append(row)

    return result
