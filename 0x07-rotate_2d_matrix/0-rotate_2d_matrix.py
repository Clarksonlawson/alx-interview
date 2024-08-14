#!/usr/bin/python3
"""
Rotate 2D matrix by 90 degrees clockwise in-place
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in place.

    Parameters:
    matrix (list of list of int): The 2D matrix to be rotated.

    Returns:
    None
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
