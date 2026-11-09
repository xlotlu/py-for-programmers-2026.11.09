def nume_functie():
    print("i am a function!")
    print("i am still a function!")

nume_functie()

def add(a, b):
    return a + b


# Scrieți o funcție
def get_greeting_for_hour(hour):
    print("doing something with", hour)
# ce returnează string-ul corect
# drept salut pt. ora respectivă a zilei

def get_greeting_for_hour(hour):
    if 5 <= hour < 10:
        return "Bună dimineața"
    elif 10 <= hour < 18:
        return "Bună ziua"
    elif 18 <= hour < 22:
        return "Bună seara"
    else:
        return "Noapte bună"

# Vrem să obținem greeting-ul pentru ora curentă
# Scrieți o funcție
def get_current_greeting():
    pass # no-op statement
# ce 1) obține ora curentă
# și 2) cheamă funcția `get_greeting_for_hour()`

# folosim clasa datetime din modulul datetime
from datetime import datetime
# clasa datetime are o metodă .now()
# ce returnează un obiect ce are atributul .hour

def get_current_greeting():
    now = datetime.now()
    hour = now.hour
    return get_greeting_for_hour(hour)

# la limita readăbilitii-ului
def get_current_greeting():
    return get_greeting_for_hour(datetime.now().hour)

# Task:
# scrieți o funcție
def greet_user():
    pass
# ce promptează utilizatorul pentru numele său,
# și face print unui string de forma
# <current_greeting> <name>!
#
# folosiți una din metodele de string interpolation.

def greet_user():
    name = input("Nume: ")
    greeting = get_current_greeting()
    print(f"o să te salut cu {greeting}, dragul meu {name}!")
