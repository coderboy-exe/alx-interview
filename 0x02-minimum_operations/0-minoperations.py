#!/usr/bin/env python3
"""Module definition: minimum number of operations Algo"""


def minOperations(n):
    """ Calculates fewest number of operations needed to result
    in exactly n 'H' characters in a file
    """
    if (n is None or n < 1):
        return 0

    operations = 0
    clipboard = 0
    text = 1

    while text < n:
        if clipboard > 0:
            # paste the clipboard
            text += clipboard
            clipboard = 0
            operations += 1
        else:
            # copy all text
            clipboard = text
            operations += 1

        # paste the copied text
        text += clipboard
        clipboard = 0
        operations += 1

    return operations
