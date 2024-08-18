# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:52:46 2024

@author: iamrs
"""

##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}


programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}



programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}


travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}




travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}



travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]