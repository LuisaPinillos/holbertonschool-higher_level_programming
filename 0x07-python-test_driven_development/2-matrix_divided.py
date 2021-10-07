#!/usr/bin/python3
"""
Function that divide each
element of the list for
a number div.
"""


def matrix_divided(matrix, div):
    """
    Div must be a integer and the lists must be
    the same lenght. If div is 0 rise error.
    """
    row = len(matrix)
    lenrow = len(matrix[0])
    matrix2 = []

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for b in range(row):
        matrix2.append([])
        for a in range(len(matrix[b])):
            if len(matrix[b]) != lenrow:
                raise TypeError("Each row of the matrix"
                                "must have the same size")
            isnotint = isinstance(matrix[b][a], (int, float))
            if isnotint is False:
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
            matrix2[b].append(round(matrix[b][a] / div, 2))
    return matrix2
