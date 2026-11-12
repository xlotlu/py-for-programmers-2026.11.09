"""
Bună dimineața,
eu sunt documentația acestui modul!
"""

# 1. dat fiind raportul primit ca string cu formatul
s = """-----------------------------------
|    Name    | Age |     City     |
-----------------------------------
| Gigel      |  20 | Copenhaga    |
| Andrei     |  42 | București    |
| Georgiana  |  20 | Timișoara    |
| Andreea    |  20 | Constanța    |
| Carmencita |  20 | Satu Mare    |
| George     |  20 | Sfântu Gheor |
-----------------------------------"""
# rescrieți funcția `parse_report()` de ieri
# astfel încât să returneze o listă de dicționare unde cheile
# sunt numele coloanelor.
#
# obțineți numele coloanelor dinamic din string-ul sursă. (don't hardcode them)

def parse_row(row):
    return [
        cell.strip()
        for cell in row[1:-1].split('|')
    ]

def parse_report(txt):
    data = txt.splitlines()
    columns = parse_row(data[1])

    out = []
    for row in data[3:-1]:
        values = parse_row(row)
        out.append(
            dict(
                zip(columns, values)
            )
        )
    return out

# sau scris cu list comprehension
def parse_report(txt):
    data = txt.splitlines()
    columns = parse_row(data[1])

    return [
        dict(
            zip(columns, parse_row(row))
        )
        for row in data[3:-1]
    ]


# 2. scrieți o funcție
def count_words(txt):
    pass
# ce numără aparițiile fiecărui cuvânt din string-ul `txt`,
# returnând un datatype potrivit acestui scop.

# Nota 1: considerați că dicționarul suportă operatorul `in`.

# Nota 2: ajutați-vă de funcția
import re # "regular expressions"

def get_words(txt: str) -> list:
    "returns the individual words in the given string"
    return re.findall(r"\w+", txt)

r"something \etc" # raw string


def count_words(txt):
    words = get_words(txt) # this is a list of words

    return {
        word: words.count(word)
        for word in words
    } # very nice. not. O(n^2)


def count_words(txt):
    words = get_words(txt) # this is a list of words

    out = {}
    for word in words:
        if word not in out:
            out[word] = 0
        out[word] += 1
    return out

# 3. dat fiind dataset-ul
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# și funcția
def get_friend_by_name(lst, name):
    #print("» looking up:", name)
    for friend in lst:
        if friend[0] == name:
            return friend
# modificați funcția astfel încât lookup-ul să fie cache-uit.



def get_friend_by_name(lst, name):
    cache = get_friend_by_name._cache

    if name in cache:
        return cache[name]

    print("» looking up:", name)
    for friend in lst:
        if friend[0] == name:
            # don't forget to populate the cache
            cache[name] = friend
            return friend
get_friend_by_name._cache = {}


# 4. transformați dataset-ul friends într-o listă de dicționare
friends_as_dicts = []
# cu cheile 'name', 'age', 'hobbies'

[
    {
        'name': 'Jane',
        'age': 20,
        'hobbies': [],
        # și mai târziu adăugăm:
        'occupation': "nurse",
    },
    #...
]

keys = 'name', 'age', 'hobbies'
friends_as_dicts = [
    dict(zip(keys, values))
    for values in friends
]

# 5. dat fiind dicționarul
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    #"Sam": "boat captain",
    "Anna": "gardner",
}
# faceți update dicționarelor din `friends_as_dicts` asfel încât
# să setați o cheie nouă "occupation" cu valoarea corespunzătoare.

for fd in friends_as_dicts:
    name = fd['name']
    try:
        occ = occupations[name]
    except KeyError:
        continue
    fd['occupation'] = occ

# 5 and a half. întrebare:
# dacă friends are 10.000.000 elemente
# și occupations vin succesiv ca update-uri parțiale.
#
# strategie?

# 1) iterăm pe occupations
# 2) cum găsim eficient elementul din friends_as_dicts
#    pe care să-l updatăm?
#    !! cu un dicționar

keys = 'name', 'age', 'hobbies'
friends_as_dicts = {
    values[0]: dict(zip(keys, values))
    for values in friends
}

# dicționarul este iterabil:
#for name in occupations: ...
# este același lucru cu:
for name in occupations.keys():
    friend = friends_as_dicts[name]
    friend['occupation'] = occupations[name]

# mai succint, luăm key & value at once:
for name, occ in occupations.items():
    friend = friends_as_dicts[name]
    friend['occupation'] = occ
