#!/usr/bin/python3
""" Module definition """
# https://stackoverflow.com/questions/14992411/understanding-change-making-algorithm
# https://www.reddit.com/r/algorithms/comments/70wo52/can_someone_please_explain_this_coinchange/


def makeChange(coins, total):
    """ Function definition: Solution using Dynamic Programming """
    # initialize values with a very high number(infinity)
    ways = [float('inf')] * (total + 1)
    ways[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if ways[i - coin] != float('inf'):
                ways[i] = min(ways[i], ways[i - coin] + 1)

    if ways[total] == float('inf'):
        return -1

    return ways[total]
