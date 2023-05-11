#!/usr/bin/python3
""" Module definition """


def rotate_2d_matrix(matrix):
    """ Rotates an n x n 2D matrix 90 deg clockwise. Returns nothing """
    n = len(matrix)

    # First, we transpose the matrix
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Reverse each column
    for i in range(n):
        matrix[i] = matrix[i][::-1]
