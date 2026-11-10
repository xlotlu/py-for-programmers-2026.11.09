# dat fiind
lst = ["ala", "bala", "porto", "cala"]

lst[0] # item access

dct = {
    "cheie": "valoare",
    "cheie2": "valoare 2",
}

dct["cheie"] # item access


# pe elementele care suportă item access numeric
# probabil este suportat și acces după "slice"

lst[1:3] # returnează o listă nouă cu 2 elemente
         # începând de la indexul 1

# 1) sintaxa completă este
#    obj[ start : stop : step  ]
#    unde step = default 1.
# 2) oricare din părți poate fi omisă.
#    dacă este omisă, intră pe default.

"""
obj[ start : stop : step  ]
obj[ start : stop ]
obj[ : stop ]
obj[ start : ]
"""
# Q: cum facem un slice invers?
# A: la fel ca un range invers.
list(range(1, 10))
list(range(9, 0, -1))

lst = ["ala", "bala", "porto", "cala"]
lst[1:3]
lst[2:0:-1]

# primele 2 elemente:
lst[:2]
# ultimele 2 elemente:
# (remeber, există indecși negativi)
lst[-2:]


# sintaxa
lst[1:3]
# este "syntactic sugar" pentru
lst[   slice(1, 3)   ]
# ... care este la rândul său syntactic sugar pentru
lst.__getitem__(slice(1, 3))
# (dar irelevant pentru noi momentan)

lst[:3]
lst[ slice(None, 3) ]

lst[-2:]
lst[ slice(-2, None) ]

# having fun with item access:
# introducing numpy

import numpy

arr = numpy.array([
    [12, 23, 34],
    [45, 56, 67],
    [78, 89, 90],
])
arr[1, 2]
# echivalent de fapt cu
arr[(1, 2)]

# merge și cu un data-type simplu, dicționarul:
dct = {
    (1, 2): "valoare",
    (3, 4): "valoare 2",
}
dct[1, 2]


arr[:2, :3]
# cu syntactic sugar înlăturat, este:

arr[  (
    slice(None, 2) ,
    slice(None, 3)
)  ]

# cum accesăm ultimele 2 coloane din arr?
arr[:, -2:]
