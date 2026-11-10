# a word about iterables in Python:
# in Python, iterables do not have to be memory-backed:
huge_iterable = range(1000000000, 1000000000000000000000)

for elem in huge_iterable:
    print(elem)
    break


for idx, elem in enumerate(huge_iterable):
    print(idx, elem)
    break

enumerate(huge_iterable) # returns an "enumerate object"
# care:
# 1) nu este memory-backed
# 2) generează valorile __doar__ când este iterat

# un exemplu din itertools:
from itertools import repeat
for x in repeat("am valoare", 5):
    print(x)

# atenție: repeat() merge și fără argumentul `times`
#for x in repeat("am valoare"):
#    print(x)

# Exercițiu:
# dat fiind setul de date
candidates = [
    ('Mara', 28),
    ('George', 16),
    ('Dragoș', 42),
    ('Ana', 74),
    ('Mircea', 31),
    ('Carmen', 17),
    ('Andreea', 38),
    ('Vasi', 61),
]
# conținând tuple de forma (name, age)
# generați o listă de string-uri de forma
'<tr class="even_or_odd"><td>nume</td><td>age</td></tr>'
# corespondentă listei de mai sus

[
    '<tr class="even"><td>Mara</td><td>28</td></tr>',
    '<tr class="odd"><td>George</td><td>16</td></tr>'
]

# folosiți iterație prin itertools.cycle()
# pentru a menține even / odd curent
from itertools import cycle

rows = []
for idx, cls in enumerate(cycle(["odd", "even"])):
    name, age = candidates[idx]

    rows.append(
        f'<tr class="{cls}"><td>{name}</td><td>{age}</td></tr>'
    )

    if idx == len(candidates) - 1:
        break
print(
    "\n".join(rows)
)


# varianta alternativă, obișnuită:

# itertools.cycle, itertools.repeat, enumerate
# sunt iteratori

colors = cycle(["odd", "even"])
for name, age in candidates:
    cls = next(colors)
    print(cls, name, age)
    # etc.

# date fiind iterabilele
cities = [
    'Cluj-Napoca',
    'Timișoara',
    'Iași',
    'Constanța',
    'Brașov'
]
# și
distances = [450, 550, 390, 225, 170]

# creați o listă de liste
# de forma [name, distance]
# considerând că numele și distanța sunt
# împerecheate 1:1

for idx, name in enumerate(cities):
    dist = distances[idx]
    (name, dist)

zip(cities, distances) # returnează un iterator
# lipește elementele din fiecare iterabil
# dat ca argument în câte o tuplă

for elem in zip(range(1000), cities, distances):
    print(elem)

for elem in zip(cycle(["odd", "even"]), cities, distances):
    print(elem)
