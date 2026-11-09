#for element in iterable:
#    do_something_with(element)
#    # etc.

tup = ("ala", "bala", "porto", "cala") # tuple

for elem in tup:
    print("»", elem)

lst = ["ala", "bala", "porto", "cala"] # list
for elem in lst:
    print("»", elem)

# introducing.... range:
range(1000000000) # un obiect iterabil
                  # care nu este memory-backed!

from time import sleep
for elem in range(1000000000):
    print(elem)
    sleep(.1) # suspendă execuția pentru atâtea secunde
# pentru a întrerupe execuția: Ctrl+C

# Task:
# printați pătratul numerelor impare
# de la 0 la 10
for num in range(0, 11):
    if num % 2 == 1:
        print(num ** 2)

# Dată fiind lista de orașe:
cities = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Brașov',
 'Craiova',
 'Galați',
 'Oradea',
 'Ploiești',
 'Brăila',
 'Arad',
 'Pitești',
 'Sibiu',
 'Bacău',
 'Târgu Mureș',
 'Baia Mare',
 'Buzău',
 'Satu Mare',
 'Suceava',
 'Focșani',
]
# printați elementele care încep cu litera "B"
for elem in cities:
    if elem[0] == "B":
        print(elem)

# Scrieți o funcție ce primind ca argument o listă
# ca `cities` de mai sus, returnează o listă nouă,
# filtrată după elementele ce încep cu caracterul `char`:
def filter_list(items, char):
    pass
# folosiți metoda .append() a listei

# pattern de acumulare:
def filter_list(items, char):
    # 1. creez obiectul nou în care voi acumula
    new_city_list = []

    # 2. iterez în sursa de date
    for elem in cities:
        # 3. filtrez
        if elem[0] == char:
            # 4. acumulez
            new_city_list.append(elem)
    # 5. returnez
    return new_city_list

filter_list(cities, "C") # --> []


# Dată fiind lista de tuple de forma
# (name, distance)
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 170),
    ('Craiova', 230),
    ('Galați', 250),
    ('Oradea', 600),
    ('Ploiești', 60),
    ('Brăila', 200),
    ('Arad', 530),
    ('Pitești', 120),
    ('Sibiu', 280),
    ('Bacău', 300),
    ('Târgu Mureș', 340),
    ('Baia Mare', 600),
    ('Buzău', 110),
    ('Satu Mare', 640),
    ('Suceava', 450),
    ('Focșani', 190),
    ('Cluj-Napoca', 451),
]
# scrieți o funcție
def filter_by_distance(clist, distance):
    pass
# ce returnează o listă nouă formată din elementele
# cu distanță <= distance.

print(filter_by_distance(cities, 300))
