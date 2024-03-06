#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    pascal_triangle = []
    if type(n) is not int or n <= 0:
        return pascal_triangle
    for i in range(n):
        current_line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                current_line.append(1)
            elif i > 0 and j > 0:
                current_line.append(pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j])
        pascal_triangle.append(current_line)
    return pascal_triangle
