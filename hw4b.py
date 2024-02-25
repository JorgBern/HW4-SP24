import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def equation1(x):
    """Calculates the value of the first equation for a given x.
    Args:
        x: The input value
    Returns:
        The result of the equation x - 3cos(x).
    Gemini assisted with the development of this function
    """
    return x - 3 * np.cos(x)

def equation2(x):
    """Calculates the value of the second equation for a given x.
    Args:
        x: The input value.
    Returns:
        The result of the equation cos(2x) * x^3.
    Gemini assisted with the development of this function
    """
    return np.cos(2 * x) * (x**3)

def find_root(equation, guess, tolerance=1e-6):
    """Attempts to find a root of the given equation near the provided guess.
    Args:
        equation: The equation function (either equation1 or equation2).
        guess: An initial guess for the root.
        tolerance: The acceptable error for a found root.
    Returns:
        The root if found within the tolerance, otherwise None.
    Gemini assisted with the development of this function
    """
    try:
        root = fsolve(equation, guess)
        # Check if the found root is within an acceptable tolerance
        if abs(equation(root)) <= tolerance:
            return root[0]
        else:
            return None  # Root found, but not accurate enough
    except ValueError:
        return None  # No root found
def find_intersection(guess):
    """Finds the intersection point of two functions near a provided guess and plots the functions
       and their intersection. This function uses the fsolve method from scipy.optimize to find the
       root of the difference between two functions, which gives the x-coordinate of the intersection
       point. The y-coordinate is then calculated by substituting the x-coordinate into either of the
       two functions.
    Parameters:
       guess: An initial guess for the x-coordinate of the intersection point.
    Returns:
       tuple: A tuple containing the x and y coordinates of the intersection point.
       Gemini assisted with the development of this function"""

    intersection_x = fsolve(lambda x: equation1(x) - equation2(x), guess)
    intersection_y = equation1(intersection_x)  # Or equation2(intersection_x)

# Visualization
    x = np.linspace(-10, 10, 200)
    plt.plot(x, equation1(x), label="x - 3cos(x)")
    plt.plot(x, equation2(x), label="cos(2x) * x^3")
    plt.scatter(intersection_x, intersection_y, color='red', label="Intersection")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
    return intersection_x[0], intersection_y[0]
def main():
    """
    This function is trying to find roots of two equations (equation1 and equation2) using
    different initial guesses. If it fails to find a root near a guess, it asks if the user
    wants to guess again. If the user guesses again and a root is found near the new
    guess, it prints the root and plots it on a graph. If the user does not want to guess again,
    it continues with the next guess. If the user’s response is not ‘y’ or ‘n’, it prints an error
    message. The process is repeated for each equation and each guess. The roots of equation1 are
    plotted on a labeled graph. The function then asks the user to make a guess at what x-coordinate
    they think the equation might intersect the other equation. The function find_intersection is then
    called to locate and plot an intersection near to the guess. The outer loop iterates over a
    list of tuples. Each tuple contains an equation and a list of initial guesses for that equation.
    I worked diligently with chatgpt to develop this function.
    """
    # Plotting
    x = np.linspace(-15, 15, 200)  # Range for plotting

    # Plot equation 1
    plt.figure(1)
    plt.plot(x, equation1(x))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of x - 3cos(x) = 0')
    plt.grid(True)
    plt.show()  # Display the plots

    # Input guesses for the first equation
    input_str = input(
        "Using the provided plots, make a guess where a root might exist in each equation, multiple guesses should be separated by commas.\nFor x - 3cos(x) = 0, your guess is:  ")
    guesses_eqn1 = [float(guess) for guess in input_str.split(',')]

    # Plot equation 2
    plt.figure(2)
    plt.plot(x, equation2(x))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of cos(2x) \u00B7 x\u00B3 = 0')
    plt.grid(True)
    plt.show()  # Display the plots

    # Input guesses for the second equation
    input_str = input("For cos(2x) \u00B7 x\u00B3 = 0, your guess is:  ")
    guesses_eqn2 = [float(guess) for guess in input_str.split(',')]
    for equation, guesses in [(equation1, guesses_eqn1), (equation2, guesses_eqn2)]:
        for i, guess in enumerate(guesses):  # Track guess index
            if equation == equation1:
                root1 = find_root(equation, guess)
                if root1 is not None:
                    print(f"Root near to guess #{i+1} for x - 3cos(x) = 0:  {root1}")
                    plt.figure(1)
                    plt.plot(root1, 0, 'ro')
                else:
                    while True:
                        response = input(f"Unable to locate root near guess {guess} for equation x - 3cos(x) = 0, guess again? (y/n): ").lower()
                        if response == 'y':
                            guess = float(input("Enter a new guess: "))
                            root1 = find_root(equation, guess)
                            if root1 is not None:
                                print(f"Root near to new guess for x - 3cos(x) = 0:  {root1}")
                                plt.figure(1)
                                plt.plot(root1, 0, 'ro')
                                break
                        elif response == 'n':
                            break
                        else:
                            print("Invalid response. Please enter 'y' or 'n'.")

            else:  # equation == equation2
                root2 = find_root(equation, guess)
                if root2 is not None:
                    print(f"Root near to guess #{i+1} for cos(2x) \u00B7 x\u00B3 = 0:  {root2}")
                    plt.figure(2)
                    plt.plot(root2, 0, 'ro')
                else:
                    while True:
                        response = input(f"Unable to locate root near guess {guess} for equation cos(2x) \u00B7 x\u00B3 = 0, guess again? (y/n): ").lower()
                        if response == 'y':
                            guess = float(input("Enter a new guess: "))
                            root2 = find_root(equation, guess)
                            if root2 is not None:
                                print(f"Root near to new guess for cos(2x) \u00B7 x\u00B3 = 0:  {root2}")
                                plt.figure(2)
                                plt.plot(root2, 0, 'ro')
                                break
                        elif response == 'n':
                            break
                        else:
                            print("Invalid response. Please enter 'y' or 'n'.")


    x = np.linspace(-15, 15, 200)  # Range for plotting

    # Check if root1 is not None before plotting
    if root1 is not None:
        plt.figure(1)
        plt.plot(x, equation1(x))
        plt.plot(root1, 0, 'ro')  # Mark root with red dot

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Plot of x - 3cos(x) = 0')
        plt.grid(True)

    plt.figure(2)
    plt.plot(x, equation2(x))
    if root2 is not None:
        plt.plot(root2, 0, 'ro')  # Mark root with red dot
    # Plot equation 2
    #plt.plot(root2, 0, 'ro')  # Mark roots with red dots
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Plot of cos(2x) \u00B7 x\u00B3 = 0')
        plt.grid(True)

    plt.show()
    while True:
        try:
            user_guess = float(input("Guess x-coordinate where the lines might intersect: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Find the intersection near the guess
    x_intersect, y_intersect = find_intersection(user_guess)
    print("The equations intersect near the point:", (x_intersect, y_intersect))
main()
