# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:25:40 2024

@author: iamrs
"""
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def simplify_expression(expression):
    return sp.simplify(expression)

def expand_expression(expression):
    return sp.expand(expression)

def solve_equation(equation):
    return sp.solve(equation)

def plot_function(expression, xlim=(-10, 10), ylim=(-10, 10)):
    x = sp.symbols('x')
    expr = sp.sympify(expression)
    f = sp.lambdify(x, expr, 'numpy')
    x_vals = np.linspace(xlim[0], xlim[1], 400)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of ' + expression)
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the Advanced Algebra Calculator!")
    while True:
        print("\nOptions:")
        print("1. Simplify Expression")
        print("2. Expand Expression")
        print("3. Solve Equation")
        print("4. Plot Function")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            expression = input("Enter the expression to simplify: ")
            result = simplify_expression(expression)
            print("Result:", result)

        elif choice == '2':
            expression = input("Enter the expression to expand: ")
            result = expand_expression(expression)
            print("Result:", result)

        elif choice == '3':
            equation = input("Enter the equation to solve (in the form 'expression = 0'): ")
            result = solve_equation(equation)
            print("Result:", result)

        elif choice == '4':
            expression = input("Enter the function to plot: ")
            plot_function(expression)

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


