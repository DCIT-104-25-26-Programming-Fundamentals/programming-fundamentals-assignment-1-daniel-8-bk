# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    """Reads a matrix from user input row by row."""
    matrix = []
    for i in range(1, rows + 1):
        row_str = input(f"Enter row {i}: ")
        row = [int(val) for val in row_str.strip().split()]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Prints a matrix in a neat grid format."""
    for row in matrix:
        print(" ".join(str(val) for val in row))


def transpose_matrix(matrix):
    """Computes the transpose of an M x N matrix."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix_a, matrix_b):
    """Computes the element-wise sum of two M x N matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Computes the matrix product A x B (size M x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += matrix_a[i][k] * matrix_b[k][j]
            row.append(cell_sum)
        result.append(row)

    return result


def main():
    # Example execution flow for reading and transposing a matrix
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("\nTransposed Matrix:")
    transposed = transpose_matrix(matrix)
    display_matrix(transposed)


if __name__ == "__main__":
    main()