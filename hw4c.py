# The order and events of code:
# press run:
# 1) prompt appears in CLI to enter number of rows in augmented matrix
# 2) prompt appears in CLI to enter number of columns in augmented matrix
# 3) prompts to enter each row will appear consecutively to fill each row
# 4) Solution to the augmented matrix is posted to the CLI
# 5) User given option to calculate another.
#
# Assumptions:
#      The user knows the dimensions of the augmented matrix and its A and b values.
import numpy as np
from scipy.linalg import solve

def get_matrix_from_user():
    """
    Prompts the user to input the size and elements of an augmented matrix.
    Returns:
        matrix (numpy.ndarray): The user-inputted augmented matrix. If the user inputs a row with a number of elements
        that doesn't match the number of columns, the function will print an error message and return None.
    """
    # Get the size of the matrix
    rows = int(input("Enter the number of rows in the augmented matrix: "))
    cols = int(input("Enter the number of columns in the augmented matrix: "))

    # Initialize an empty matrix
    matrix = []

    # Get each row of the matrix
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i+1} of the matrix (separate numbers with spaces): ").split()))
        # Check if the number of elements in the row matches the number of columns
        if len(row) != cols:
            print("Error: The number of values in this row does not match the number of columns.")
            return None
        matrix.append(row)

    return np.array(matrix)

def solve_system():
    """
    Continuously prompts the user to input augmented matrices and solves the corresponding
    systems of equations until the user chooses to stop.
    If the system of equations cannot be solved, the function will print an error message
    and prompt the user to input another system.
    """
    # Define subscript numbers as a dictionary
    subscript = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉"}

    while True:
        # Get the augmented matrix from the user
        matrix = get_matrix_from_user()

        # If the user inputted a row with a number of elements that doesn't match the number of columns, prompt them to input another system
        if matrix is None:
            continue

        # Separate the matrix A from the column vector b
        A, b = matrix[:, :-1], matrix[:, -1]

        # Solve the system
        try:
            x = solve(A, b)
            # Round the solutions to the nearest 1e4
            x = np.around(x, decimals=4)
            # Print each solution on a new line with the desired format
            for i, xi in enumerate(x, start=1):
                # Convert the index to a string and replace each digit with its subscript equivalent
                subscript_i = "".join(subscript[digit] for digit in str(i))
                print(f"x{subscript_i} = {xi}")
        except Exception as e:
            print("Error: Could not solve the system of equations.")
            print("Details:", str(e))

        # Ask the user if they want to solve another system
        again = input("Would you like to solve another system? (y/n): ")
        if again.lower() != "y":
            break


if __name__ == "__main__":
    solve_system()
