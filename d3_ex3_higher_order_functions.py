# list.sort() cu argumentul key reprezintă un
# "higher order function"

# 1. list.sort()

people = [
    ['Tudor', 17],
    ['Brian', 17],
    ['Gigel', 20],
    ['Andrei', 42],
    ['Georgiana', 20],
    ['Andreea', 42],
    ['Carmencita', 22],
    ['George', 41],
    ['Vasi', 61],
    ['Mircea', 61],
]
# sortați lista în ordine crescătoare
# după vârstă și nume

def sorter(elem):
    return (elem[1], elem[0])
people.sort(key=sorter)


# introducing lambda functions
#lambda: return_value
#lambda arg1, arg2: return_value
my_func = lambda: True
my_func()

mul_5 = lambda x: x * 5
mul_5(2)

people.sort(key=lambda elem: (elem[1], elem[0]))


# 2. filter()

# new task:
# dată fiind structura de date `people` de mai sus
# creeați un iterabil cu persoanele cu vârstă
# între 18 și 60 de ani inclusiv.

# introducing: `filter(function, iterable)`

def filterer(elem):
    return 18 <= elem[1] <= 60

for elem in filter(filterer, people):
    print(elem)

# același lucru, dar cu lambda
filtered = filter(
    lambda elem: 18 <= elem[1] <= 60,
    people
)
#print(filtered) # un iterator
print(
    list(filtered)
)


# 3. sorted()
# sorted(iterable, key=..., reverse=...)

# face același lucru ca list.sort()
# doar că primește iterabilul drept prim argument
# și returnează o listă (nouă).

sorted(people, key=lambda elem: (elem[1], elem[0]))
# ^^ același lucru ca mai devreme dar a returnat o listă nouă

# dacă am vrea oamenii filtrați după vârstă
# și sortați după (vârstă, nume)?
filtered = filter(
    lambda elem: 18 <= elem[1] <= 60,
    people
)
print(
    sorted(filtered, key=lambda elem: (elem[1], elem[0]))
)

# Exercițiu:
# scrieți o funcție
MIN_AGE = 18
MAX_AGE = 60
def filter_candidates(candidates,
                      min_age=MIN_AGE, max_age=MAX_AGE,
                      sort=True, limit=None):
    pass
# care filtrează lista de candidați conform min_age și max_age
# (considerați că sunt întotdeauna definite)
# și returnează o listă nouă sortată conform argumentului `sort`:
# dacă sort == True, sortează după (age, name) altfel îi lasă nesortați
# și limitează numărul de elemente la `limit` dacă limit is not None.

def filter_candidates(candidates,
                      min_age=MIN_AGE, max_age=MAX_AGE,
                      sort=True, limit=0):
    # 1. filtrarea
    filtered = filter(
        lambda elem: min_age <= elem[1] <= max_age,
        candidates
    )

    # 2. sortarea
    if sort:
        results = sorted(
            filtered,
            key=lambda elem: (elem[1], elem[0])
        )
    else:
        results = list(filtered)

    #if limit is None:
    #    return results
    #else:
    #    return results[:limit]

    return results if limit is None else results[:limit]


# rewrite pentru minimalism și logică:
def filter_candidates(candidates,
                      min_age=MIN_AGE, max_age=MAX_AGE,
                      sort=True, limit=0):
    results = list(filter(
        lambda elem: min_age <= elem[1] <= max_age,
        candidates
    ))

    # 2. sortarea
    if sort:
        results.sort(
            key=lambda elem: (elem[1], elem[0])
        )

    if limit is None:
        return results
    else:
        return results[:limit]

filter_candidates(people)
filter_candidates(people, limit=3)
filter_candidates(people, sort=False)


# 4. map

def add5(x):
    return x + 5
map(add5, range(10))
print(
    list(map(add5, range(10)))
)

# dată fiind lista people de mai sus,
# vrem să o transformăm într-o listă de dicționare.

# știind că sintaxa de definire a unui dicționar este
{
    'key 1': 'value 1',
    'key 2': 'value 2',
}

# vrem să scriem o funcție ce primind un element
# [name, age]
# returnează un dicționar
# {
#     "name": name,
#     "age": age,
# }
def person_to_dict(person):
    name, age = person

    return {
        "name": name,
        "age": age,
    }

print(
    list( map(person_to_dict, people) )
)

from functools import partial
# partial este o funcțiue ce primește ca argument o funcție
# și returnează o altă funcție

def multiply(x, y):
    return x * y
mul_5 = partial(multiply, y=5)

print(
    mul_5(2), mul_5(3), mul_5(4)
)

# sau...

def http_request(method, payload):
    pass

# în loc de:
def get(payload):
    return http_request('GET', payload)
def post(payload):
    return http_request('GET', payload)

# putem scrie:
get = partial(http_request, method='GET')
post = partial(http_request, method='POST')
