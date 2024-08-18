# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:51:32 2023

@author: mithun sai
"""
#This code created by mithun sai
#This code about access tuple
#Access tuple items
thistuple=("apple","banana","cherry")
print(thistuple[1])#In this bracket we can the number thistuple we have to add any word
#Negative indexes
thistuple=("apple","banana","cherry")
print(thistuple[-1])
#Range indexes 
thistuple=("apple","banana","cherry","orange","Kiwi","melon","mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:2])
#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4:-1])
#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")