#!/usr/bin/python3
'''Rotation  of 2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 90° clockwise
    Returns: Nothing at all
    '''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save topleft first
            topLeft = matrix[top][left + i]
            # move bottomleft to topleft
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottomright to bottomleft
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move topright to bottomright
            matrix[bottom][right - i] = matrix[top + i][right]
            # move topleft to topright
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
