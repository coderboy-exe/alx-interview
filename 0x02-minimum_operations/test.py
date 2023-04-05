def minOperations(n):
    """
    Calculates fewest number of operations needed to result
    in exactly n 'H' characters in a file
    """
    if n is None or n < 1:
        return 0

    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    return operations
