#!/usr/bin/python3
""" Function that divides all element of a matrix
Args: matrix: list of list of integers or floats
      div: divisor must be a number (integer or float)
Returns: a new matrix with all elements divided by div, rounded to 2 decimal
Raises: TyperError: if matrix is not a list of list of integers/floats
                    if each row of the matrix is not of the same size
                    if div is not a number
        ZeroDivisionError: if div is zero"""
def matrix_divided(matrix, div):
    """Function that divides all element of a matrix
    Returns a result rounded at 2 decimal"""
    if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
    