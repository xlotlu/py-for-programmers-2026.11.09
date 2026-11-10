# dat fiind algoritmul

header = "|   Name   |   Home Address  |    Phone    |"

columns = []
for col in header.strip("|").split("|"):
    columns.append(col.strip())

# putem rescrie construcția listei de mai sus astfel:
#[    procesare(elem)    for elem in iterable     ]

[col.strip() for col in header.strip("|").split("|")]

# ceva mai simplu:
lst = []
for elem in range(5):
    lst.append(elem ** 2)

[
    elem ** 2
    for elem in range(5)
]

[elem ** 2 for elem in range(5)]


# adăugam if la mix:
lst = []
for elem in range(10):
    if elem % 2:
        lst.append(elem ** 2)
# se transformă în
[
    elem ** 2
    for elem in range(10)
    if elem % 2
]

columns = []
for item in header.split("|"):
    if item != '':
        columns.append(item.strip())
# se transformă în:
[
    item.strip()
    for item in header.split("|")
    if item != ''
]


# Exercițiu:
# rescrieți funcția
def find_friends_by_hobby(friends, hobby):
    out = []
    for elem in friends:
        if hobby in elem[2]:
            out.append(elem)
    return out
# astfel încât să returneze o listă
# formată cu comprehension


# list comprehension multi-dimensional
matrix = [
    ["ab", "bc", "cd"],
    ["mn", "no", "op"],
    ["wx", "xy", "yz"],
]
# vrem să facem flatten la toată matricea
lst = []
for row in matrix:
    for cell in row:
        lst.append(cell)
print(lst)
# cu comprehension:
[cell for row in matrix for cell in row]

# dar pentru a crea o listă cu elementele din diagonală?

# introducem enumerate și iterable unpacking:
lst = ["ala", "bala", "porto"]
enumerate(lst)



# multiple variable assignment
a, b = 1, 2
# se numește "iterable unpacking", pentru că
a, b = [1, 2]
a, b = range(2)
idx, value = (1, "something")

# combinat cu enumerate:
for elem in enumerate(lst):
    idx, value = elem

# doar că merge și în interiorul for-ului:
for idx, value in enumerate(lst):
    print(idx, value)

# vrem să creăm o listă cu elementele din diagonala matricei
lst = []
for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        if i == j:
            lst.append(cell)

# cu comprehension
[
    cell
    for i, row in enumerate(matrix)
    for j, cell in enumerate(row)
    if i == j
]

# sau, algoritmul clasic
"""
for (i=0; i<matrix.length; i++) {
    for (j=0; i<matrix[i].length; j++) {
        matrix[i][j]
    }
}
"""
lst = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            lst.append(matrix[i][j])
# scris cu comprehension
[
    matrix[i][j]
    for i in range(len(matrix))
    for j in range(len(matrix[i]))
    if i == j
]


