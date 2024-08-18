# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 17:21:34 2024

@author: iamrs
"""

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])

programming_dictionary["loop"] = {"the action of mithun"}
print(programming_dictionary)

programming_dictionary["bug"]="monkey man"
print(programming_dictionary      )

for key in programming_dictionary:
    print(key)
    print(programming_dictionary)