import cmath

def quadratic_formula(a, b, c):
    # Calculate the discriminant
    discriminant = (b**2) - (4*a*c)

    # Find two solutions
    solution1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    solution2 = (-b + cmath.sqrt(discriminant)) / (2*a)

    return solution1, solution2

# Get coefficients from the user
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Call the quadratic_formula function
solution1, solution2 = quadratic_formula(a, b, c)

# Print the solutions
print(f"The solutions to the quadratic equation are: {solution1} and {solution2}")
