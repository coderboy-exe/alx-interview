#!/usr/bin/python3
""" Module definition for n-queens problem """
import sys


def backtrack(n, r, col, pos_diag, neg_diag, board, result, valid):
    """ recursive function to check different placements """
    if r == n:
        copy = [row.copy() for row in board]
        result.append(copy)
        return

    for c in range(n):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue

        col.add(c)
        pos_diag.add(r + c)
        neg_diag.add(r - c)
        board[r][c] = [r, c]

        valid.append(board[r][c])

        backtrack(n, r + 1, col, pos_diag, neg_diag, board, result, valid)

        col.remove(c)
        pos_diag.remove(r + c)
        neg_diag.remove(r - c)
        board[r][c] = 0
    return result


def solve(n):
    """ initializes trackers and call recursive function """
    col = set()
    pos_diag = set()
    neg_diag = set()

    result = []
    valid = []
    board = [[0] * n for i in range(n)]

    backtrack(n, 0, col, pos_diag, neg_diag, board, result, valid)

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = solve(n)

    for res in results:
        valid_results = []
        for row in res:
            valid_row = []
            for cell in row:
                if cell != 0:
                    valid_row.extend(cell)
            valid_results.append(valid_row)
        print(valid_results)
