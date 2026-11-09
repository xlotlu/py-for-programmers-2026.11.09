#if conditie:
#    statement
#    statement
#    etc.

age = 22

if age < 18:
    print("You are too young")
else:
    print("you are accepted")

# if(age < 18) {
#     print("You are too young")
# } else {
#     print("you are accepted")
# }

# Task:
# cereți utilizatorului vârsta
# dacă este mai mic de 18 ani
# este respins, altfel este acceptat
age = input("Vârsta ta? ")
age = int(age)

if age >= 18:
    print("You are accepted")
else:
    print("You are too young")


# Dată fiind ora curentă
hour = 11
# Scrieți un condițional care să printeze
# salutul potrivit acestei ore:
# 
# între 5 și 10:  "Bună dimineața"
# între 10 și 18: "Bună ziua"
# între 18 și 22: "Bună seara"
# între 22 și 5:  "Noapte buna"


"""
# if, complet:
# v.1.
if condition:
    statements

# v.2.
if condition:
    statements
else:
    statements

# v.3.
if condition1:
    statements
elif condition2:
    statements
# ... și oricâte alte elif-uri

# v.4, full
if condition1:
    statements
elif condition2:
    statements
elif condition3:
    statements
#... etc.
else:
    statements
"""


if hour >= 5 and hour < 10:
    print("Bună dimineața")
if hour >= 10 and hour < 18:
    print("Bună ziua")
if hour >= 18 and hour < 22:
    print("Bună seara")
if hour >= 22 or hour < 5:
    print("Noapte buna")

if hour >= 5 and hour < 10:
    print("Bună dimineața")
elif hour >= 10 and hour < 18:
    print("Bună ziua")
elif hour >= 18 and hour < 22:
    print("Bună seara")
else:
    print("Noapte bună")

# în Python există operator chaining
if 5 <= hour < 10:
    print("Bună dimineața")
elif 10 <= hour < 18:
    print("Bună ziua")
elif 18 <= hour < 22:
    print("Bună seara")
else:
    print("Noapte bună")
