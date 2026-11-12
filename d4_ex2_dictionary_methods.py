# dictionary methods

dict.fromkeys(range(10, 16))
# ^^ a classmethod that is a factory method

# with a default value:
dict.fromkeys("abcd", '-- default --')


d = {
    "Brașov": 100,
    "București": 50,
}

# iterating dictionaries:

for k in d.keys():
    pass

for v in d.values():
    pass

for k, v in d.items():
    pass


# .get()
# avoids try / except:
d.get("Brașov") # --> 100
d.get("BrașovX") # --> None
d.get("BrașovX", 0) # --> 0

from d4_ex1_morning_practice import get_words

def count_words(txt):
    words = get_words(txt) # this is a list of words

    out = {}
    for word in words:
        count = out.get(word, 0)
        out[word] = count + 1
    return out


# .setdefault()
# sets the key if not exists:
d.setdefault("Brașov", 200) # --> 100 (existing)
d.setdefault("Constanța", 200) # --> 200 (creates new key)


# .clear()
# .copy()


# .pop(key)
d.pop("Brașov") # --> 100 and removes the item
#d.pop("Brașov") # --> KeyError


# .popitem()

# Task: consumați dicționarul în timp ce iterați pe el
while d:
    k, v = d.popitem()
    # do something with k, v


# .update()
# in-place update with the given elements
d.update({
    "Brașov": 103,
    "Constanța": 200,
    "Wherever": 500,
})
# this also works:
d.update(Brașov=105, Elsewhere=102)


# Exercițiu:
# dat fiind dicționarul
dcities = {
    'Cluj-Napoca': 449,
    'Timișoara': 550,
    'Iași': 390,
    'Constanța': 225,
    'Brașov': 170,
    'Craiova': 230,
    'Galați': 250,
    'Oradea': 600,
    'Ploiești': 60,
    'Brăila': 200,
    'Arad': 530,
    'Pitești': 120,
    'Sibiu': 280,
    'Bacău': 300,
    'Târgu Mureș': 340,
    'Baia Mare': 600,
    'Buzău': 110,
    'Satu Mare': 640,
    'Suceava': 450,
    'Focșani': 190
}
# creați un dicționar nou cu elementele
# ordonate în ordinea descrescătoare a distanțelor
dict(
    sorted(
        dcities.items(),
        key=lambda elem: elem[1],
        reverse=True
    )
)
