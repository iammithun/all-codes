# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:42:12 2023

@author: iamrs
"""


size = 10000


for i in range(size):
    if i < size // 2:
        print(" " * (size // 2 - i) + "@$*()!#^&" + " " * (2 * i - 1) + "@$*()!#^&*" * (i != 0))
    else:
        print(" " * (i - size // 2) + "@$*()!#^&" + " " * (2 * (size - i) - 3) + "@$()!#^&*" * (i != size - 1))


age=1
if age>=18:
    print("You vote in this age")
    print("what is your name")
else:
    print("you are very young you can't vote you can vote after 1 year")
    print("sorry . i can't do anything")

 
age=3
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $50.")
    
age=12
if age<4:
    price=0
elif age<18:
    price=25
else:
    price=50
    
print("Your admission cost ${10000}.")

alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points']) 

alien_0={'color':'green','points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

def print_diamond(height):
    if height % 2 == 0:
        height += 1  # Ensure the height is an odd number

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "*" * i)

diamond_height = 10
print_diamond(diamond_height)

def print_diamond(height):
    if height % 2 == 0:
        height += 1  # Ensure the height is an odd number

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "$" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "$" * i)

diamond_height = 10
print_diamond(diamond_height)


def print_diamond(height):
    if height % 2 == 0:
        height += 1  # Ensure the height is an odd number

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "@" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "@" * i)

diamond_height = 10
print_diamond(diamond_height)

def print_diamond(height):
    if height % 2 == 0:
        height += 1  # Ensure the height is an odd number

    for i in range(1, height + 1, 2):
        spaces = (height - i) // 2
        print(" " * spaces + "%" * i)

    for i in range(height - 2, 0, -2):
        spaces = (height - i) // 2
        print(" " * spaces + "%" * i)

# Example usage:
diamond_height = 10
print_diamond(diamond_height)

