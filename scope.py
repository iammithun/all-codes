# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:11:13 2024

@author: iamrs
"""

player_health=10

def game():
  def drink_potion():
      potion_strenght=2
      
  drink_potion()
  
print(player_health)



enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


game_level=3
def create_enemy():
 enemies=["zombie", "skeleton", "alien" ]
 if game_level<5:
   new_enemy=enemies[0]
    
 print(new_enemy)
 
 
 enemies = "alien"

def increase_enemies():
  enemies = "zombie"
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 1

def increase_enemies():
  enemies=0
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 1

def increase_enemies():

  print(f"enemies inside function: {enemies}")
  return enemies + 1
increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 1

def increase_enemies():

  print(f"enemies inside function: {enemies}")
  return enemies + 1
eneimes=increase_enemies()
print(f"enemies outside function: {enemies}")