lst = ["ala", "bala", "porto", "cala", "ala", "bala", "ala"]


# .count() și .index() sunt comune tuturor sequences
lst.count("ala")  # --> 3
lst.count("bala") # --> 2

lst.index("ala")  # --> 0
lst.index("bala") # --> 1
# cu argument opțional start:
lst.index("ala", 1)  # --> 4

#lst.index("does not exist")
# raises ValueError

###
# comentariu lateral:
# .index() are același behaviour la toate sequences.
# la string însă există și metoda
# .find() care face exact același lucru,
# dar dacă nu găsește indexul returnează -1
###


# manipulating lists

#.append() # one item
lst.append("ceva!!!")

#.extend() # more items
lst.extend(["un elem", "doi elem"])

#.insert() # adaugă la indexul dat
lst.insert(1, "ceva nou")
# notă despre insert: forțează reindexarea listei

#.pop() # remove and return the last item
lst.pop()
# or remove and return the item at index:
lst.pop(1)
# aceeași notă: implică reindexarea listei


# LIFO: last-in, first-out
l = []
l.append("un elem")
l.append("doi elem")
l.append("trei elem")

l.pop()
l.pop()
l.pop()

# FIFO: first-in, first-out
l = []
l.append("un elem")
l.append("doi elem")
l.append("trei elem")

l.pop(0) # implică reindexare când scoatem item-urile
l.pop(0)
l.pop(0)

# alternativ:
l = []
l.insert(0, "un elem") # implică reindexare când inserăm item-urile
l.insert(0, "doi elem")
l.insert(0, "trei elem")

l.pop()
l.pop()
l.pop()

# .remove()
lst.remove("ala")

# dacă am scrie o funcție
def remove_first_from_lst(lst, value):
    for idx, elem in enumerate(lst):
        if elem == value:
            del lst[idx]
            return
    # if we got here, the value is not within the list
    raise ValueError("value does not exist")

try:
    remove_first_from_lst(lst, "something")
except ValueError:
    print('"something" was not in list')

# scrieți o funcție
def remove_all_from_lst(lst, value):
    pass
# fiind cât mai succinți, și folosind din plin
# puterea deja expusă a Python-ului

# strategie
def remove_all_from_lst(lst, value):
    while True:
        try:
            lst.remove(value)
        except ValueError:
            return

lst = ["ala", "bala", "porto", "cala", "ala", "bala", "ala"]
remove_all_from_lst(lst, "ala")
print(lst)


# and finally,
lst.clear() # does the obvious.


### celelalte metode:
# .copy() returns a new list
lst = ["ala", "bala", "porto"]
lstx = lst
lsty = lst.copy()
lst.append("ceva")
print(len(lst), len(lstx), len(lsty)) # 4, 4, 3

# notă: .copy() returnează "a shallow copy"
lst = ["ala", "bala", "porto", ["something"]]
clone = lst.copy()
lst[3].append("ok...")
# se reflectă și în clonă:
clone[3] == lst[3]
# pentru că de fapt!
clone[3] is lst[3]

# pentru situațiile în care vrem deep copy:
from copy import deepcopy
clone = deepcopy(lst)
lst[3] == clone[3]
clone[3] is not lst[3]
lst[3].append("wow")
lst[3] != clone[3]

# .sort(): sortare in-place
lst = [1, 2, 15, 7, 5, 2]
lst.sort()

# .reverse(): tot in-place
lst.reverse()

# .sort() primește și argument reverse
lst.sort(reverse=True) # face o singură re-indexare


# întrebare: cum sortăm această structură de date
#            după distanță?
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

def sorter(elem):
    return elem[1]
cities.sort(key=sorter)


# Exercițiu: dată fiind lista de liste de forma
# [name, age]
people = [
    ['Gigel', 20],
    ['Andrei', 42],
    ['Georgiana', 20],
    ['Andreea', 42],
    ['Carmencita', 22],
    ['George', 41]
]
# sortați lista în ordine crescătoare
# după vârstă și nume

def sorter(elem):
    return (elem[1], elem[0])
people.sort(key=sorter)
