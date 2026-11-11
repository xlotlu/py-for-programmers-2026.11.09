d = {
    'key1': 'value 1',
    'key2': 'value 2',
}

# pe ambele părți ale :
# se păstrează sintaxa de Python obișnuită:
k1 = "something"
k2 = "something else"

d = {
    k1: "value 1",
    k2: "value 2",
}

# item assignment:
d['key3'] = 'new value'
# the same with changing an existing value:
d['key1'] = 'modified'

# pattern-uri de lucrat cu dicționare
# 1: stilul id->value
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
    ('Cluj-Napoca', 449),
]
# creați din lista cities un dicționar
# în care cheile sunt numele, respectiv
# valorile sunt distanțele 

# pattern de acumulare:
# 1. creăm un dicționar gol
d = {}
# 2. iterăm peste sursa de date
for name, distance in cities:
    # 3. asignăm valorile
    d[name] = distance
print(d)

# 1: stilul listă de dicționare
# creați din lista cities o listă nouă
# în care fiecare element este un dicționar
# de forma {'city': name, 'distance': distance}
d_cities = []
for name, distance in cities:
    d_cities.append({
        'name': name,
        'distance': distance,
    })
# cu list comprehension?
d_cities = [
    {
        'name': name,
        'distance': distance,
    }
    for name, distance in cities
]

# revizităm acumularea într-un dicționar
# (pattern-ul #1)
# și rescriem cu dict comprehension:
d = {}
for name, distance in cities:
    d[name] = distance
print(d)

{
    name: distance
    for name, distance in cities
}


# alte modalități de a instanția dicționarul:

# A. cu keyword arguments
dict(key1="value 1", key2="value 2")
# ^^ sintaxa aceasta ne limitează la chei care:
# 1. sunt string-uri, și
# 2. sunt valid identifiers

# dict(key 1="value 1", key2="value 2") # imposibil
# dict(2_key1="value 1", key2="value 2") # imposibil

# B. dintr-un iterabil
#    ale cărui elemente sunt la rândul lor
#    iterabile cu 2 elemente

# Exercițiu de gândire (și implementare):
# Scenariu: dataset-ul `cities` își schimbă structura des:
#           a apărut întâi coloana "altitude",
#           apoi a apărut "population",
#           și tocmai ni s-a cerut să adăugăm și "latitude" & "longitude"
d_cities = []
for name, distance, altitude, population in cities:
    d_cities.append({
        'name': name,
        'distance': distance,
        'altitude': altitude,
        'population': population,
    })
# this is where I'm done și o să abstractizez problema.
from config import CITIES_COLUMNS
# "name", "distance", "altitude", "population", "latitude", "longitude"

cities = [
    ('Cluj-Napoca', 450, 883, 541000, 44.36, 22.08),
    ('Timișoara', 550, 1156, 724000, 44.74, 22.61),
    ('Iași', 390, 1049, 326000, 44.95, 22.26),
    ('Constanța', 225, 614, 484000, 44.3, 22.24),
    ('Brașov', 170, 931, 526000, 44.57, 22.49),
    ('Craiova', 230, 679, 291000, 44.99, 22.45),
    ('Galați', 250, 952, 428000, 44.3, 22.52),
    ('Oradea', 600, 1159, 549000, 44.05, 22.11),
    ('Ploiești', 60, 870, 291000, 44.8, 22.87),
    ('Brăila', 200, 702, 428000, 44.55, 22.1),
    ('Arad', 530, 1131, 770000, 44.86, 22.69),
    ('Pitești', 120, 1106, 540000, 44.72, 22.74),
    ('Sibiu', 280, 839, 347000, 44.39, 22.39),
    ('Bacău', 300, 1086, 580000, 44.14, 22.1),
    ('Târgu Mureș', 340, 868, 293000, 44.96, 22.84),
    ('Baia Mare', 600, 1191, 259000, 44.78, 22.73),
    ('Buzău', 110, 956, 757000, 44.59, 22.18),
    ('Satu Mare', 640, 1194, 378000, 44.34, 22.64),
    ('Suceava', 450, 1187, 469000, 44.0, 22.04),
    ('Focșani', 190, 1005, 750000, 44.39, 22.8),
    ('Cluj-Napoca', 449, 1173, 414000, 44.4, 22.47)
]

# pentru fiecare element din dataset
# folosim din CITIES_COLUMNS, de la același index, valoarea drept cheie

as_dicts = [
    {
        'name': 'Cluj-Napoca',
        'distance': 450,
        'population': 25000,
        # ...
    },
    # ....
]

d_cities = []
for elem in cities:
    d = {}
    # îi populăm lui `d` perechile cheie-valoare

    for idx, column in enumerate(CITIES_COLUMNS):
        d[column] = elem[idx]

    d_cities.append(d)

# much shorter, zip to the rescue:
[
    dict(zip(CITIES_COLUMNS, elem))
    for elem in cities
]

