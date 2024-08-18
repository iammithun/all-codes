# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:01:32 2023

@author: iamrs
"""


current_number=9
while current_number<10:
    current_number+=1
    if current_number %1==9:
        continue
    
    print(current_number)
    
family=['saravanan','preethi','mithun sai','omkar']#list
print(family)
print(family)
while 'mithun sai' in family:
    family.remove('saravanan')
    family.remove('mithun sai')
    family.append('linga')
    family.append('ramlingam')
    family.insert(1,'sai')
print(family)

family=['saravanan','preethi','mithun sai','omkar']#list 
tropical=['sai','linga','ramlinam']
while 'mithun sai' in family:
    family.remove('mithun sai')
    family.extend(tropical)
print(family)    


word_list = ["Hello", "world", "this", "is", "a", "list"]
joined_string = ""

index = 0


while index < len(word_list):

    joined_string += word_list[index]
    
    if index < len(word_list) - 1:
        joined_string += " "
    index += 1

print(joined_string)

{"dosa","idle","sambar rice","porri","chapathi"}

name="preethi"
mithun=['dosa', 'idli']
omkar=['chapath', 'poori']

if name <= "mithun":
    print("dosa","idli")
    print("dosa","idle")
    
elif name <="omkar":
    print("porri","chapathi")
        
else:
    print("sambar rice")

    

menu={
     "idly":2.50,
    "Dosa": 4.00,
    "Sambar Rice": 5.00,
    "Poori": 3.00,
    "Chapati": 2.00
}

for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

mithuns_order = ["Idly", "Dosa", "Sambar Rice"]  
total_price = 0.0
for item in mithuns_order:
    if item in menu:
        item_price = menu[item]
        print(f"{item} is available for ${item_price:.2f}.")
        total_price += item_price
    else:
        print(f"{item} is not available in our menu.")

print(f"Total Bill: ${total_price:.2f}")


    