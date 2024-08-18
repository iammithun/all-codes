import math

def pythagorean_theorem(a, b):
    """
    Calculate the length of the hypotenuse of a right triangle
    given the lengths of the other two sides using the Pythagorean theorem.
    
    Arguments:
    a -- Length of one side of the triangle
    b -- Length of the other side of the triangle
    
    Returns:
    Length of the hypotenuse
    """
    return math.sqrt(a**2 + b**2)

def main():
    print("Pythagorean Theorem Calculator")
    print("-----------------------------")
    a = float(input("Enter the length of one side (a): "))
    b = float(input("Enter the length of the other side (b): "))
    hypotenuse = pythagorean_theorem(a, b)
    print("The length of the hypotenuse is:", hypotenuse)

if __name__ == "__main__":
    main()
