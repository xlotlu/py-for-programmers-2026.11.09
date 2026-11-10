# 1. partea întreagă a împărțirii lui 17 la 4


# 2. restul împărțirii lui 17 la 4


# 3. 2 la puterea a 8a?


# 4. repetați (concatenați cu sine) string-ul "bla" de 7 ori


# 5. scrieți o funcție `cube(x)` ce returnează cubul lui x


# 6. luați input de la utilizator cu un număr întreg și
#    faceți apoi print string-ului
#    "Cubul numărului <num> este <cub>."
#    folosind funcția cube de mai sus.


# 7. dată fiind următoare structură de date
#    separați elementele sale în două liste noi
#    `accepted` și `rejected`, astfel încât persoanele
#    cu vârsta între 18 și 60 sunt accepted, restul rejected.
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
#   ștind că metoda .pop() a listei scoate ultimul element din listă
#   și îl returnează, consumați lista-sursă în timpul iterației.
#   (adică la sfârșitul iterației lista va fi goală)
accepted = []
rejected = []
while candidates:
    item = candidates.pop()

    if 18 <= item[1] <= 60:
        accepted.append(item)
    else:
        rejected.append(item)

    # sau:
    #target = accepted if 18 <= item[1] <= 60 else rejected
    #target.append(item)


# 8. dată fiind structura de date care este o listă de liste
#    [name, age, hobbies]
friends = [
    ['Jane', 20, ['reading', 'hiking', 'biking']],
    ['Mike', 17, ['hiking', 'fishing']],
    ['Anna', 25, []],
    ['Sam', 40, ['playing guitar']],
    ['Dan', 34, ['painting', 'reading']]
]
#    scrieți o funcție
def get_friend_by_name(friends, name):
    pass
#    ce returnează elementul (prietenul) cu acel nume.

def get_friend_by_name(friends, name):
    for friend in friends:
        if friend[0] == name:
            return friend

# 9. folosind funcția de mai sus, faceți următoarele operațiuni:
#    - găsiți-o pe Jane și îmbătrâniți-o cu un an (a fost ziua ei)
#    - folosind metoda .append() a listei adăugați-i lui Sam
#      hobby-ul "hiking"
#    - folosind metoda .extend() a listei, ce primește ca argument un
#      iterabil, adăugați-i Annei hobby-urile "knitting" și "biking"
#    - ștergeți-i lui Mike ultimul hobby folosind statement-ul del
#      și acces după index.
#
#    inspectați lista inițială friends. ce observați?
jane = get_friend_by_name(friends,"Jane")
jane[1] += 1

sam = get_friend_by_name(friends,"Sam")
sam[2].append("hiking")

anna = get_friend_by_name(friends,"Anna")
anna.extend(["knitting", "biking"])

mike = get_friend_by_name(friends,"Mike")
del mike[2][-1]

# 10. scrieți două funcții
def find_friends_by_hobby(friends, hobby):
    pass
# ce returnează o listă nouă cu prietenii cu acel hobby.
#
# folosiți operatorul boolean `in`:
# if item in iterable:...

def find_friends_by_hobby(friends, hobby):
    out = []
    for elem in friends:
        if hobby in elem[2]:
            out.append(elem)
    return out

# și
def find_friends_by_age(friends, min_age=None, max_age=None):
    pass
# ce returnează o listă nouă cu prietenii între acele vârste.
# dacă unul din argumente este `None`, atunci nu aplicați
# respectivul min / max.

# v.1.: iterăm și excludem ce nu se potrivește
def find_friends_by_age(friends, min_age=None, max_age=None):
    result = []
    for friend in friends:
        age = friend[1]
        if min_age is not None and age < min_age:
            continue
        if max_age is not None and age > max_age:
            continue
        result.append(friend)
    return result

# v.2.: iterăm și includem cu un mare if
def find_friends_by_age(friends, min_age=None, max_age=None):
    out = []
    for elem in friends:
        age = elem[1]
        if (
            (min_age is None or age >= min_age)
            and
            (max_age is None or age <= max_age)
        ):
            out.append(elem)
    return out

# v.3.: același lucru dar delegăm if-urile la funcții definite local
def find_friends_by_age(friends, min_age=None, max_age=None):
    out = []

    def check_min_age(age):
        return min_age is None or age >= min_age

    def check_max_age(age):
        return max_age is None or age <= max_age

    for elem in friends:
        age = elem[1]
        if check_min_age(age) and check_max_age(age):
            out.append(elem)
    return out

# v.4.: același lucru, dar definim funcții condițional
#       evitând să verificăm repetat if min/max_age is None
def find_friends_by_age(friends, min_age=None, max_age=None):
    out = []

    if min_age is None:
        def check_min_age(age):
            return True
    else:
        def check_min_age(age):
            return age >= min_age

    if max_age is None:
        def check_max_age(age):
            return True
    else:
        def check_max_age(age):
            return age <= max_age

    for elem in friends:
        age = elem[1]
        if check_min_age(age) and check_max_age(age):
            out.append(elem)



find_friends_by_age(friends, min_age=15)
find_friends_by_age(friends, max_age=40)
find_friends_by_age(friends, min_age=15, max_age=40)

# să aflăm toți prietenii care fac "hiking"
# cu vârstă între 20 și 40:
find_friends_by_hobby(
    find_friends_by_age(friends, min_age=20, max_age=40),
    "hiking"
)
# și le punem flag-ul
{"buddy": True}

for buddy in find_friends_by_hobby(
    find_friends_by_age(friends, min_age=20, max_age=40),
    "hiking"
):
    buddy.append({"buddy": True})

print(friends)