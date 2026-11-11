# 1. dat fiind string-ul
s = "Ce frumos e să scrii Python!"

# a) obțineți substringul de la caracterele
# 4 la 12 inclusiv
s[3:12]
# caracterul 4 = indexul 3.
# caracterul 12 = indexul 11.
# dar ultimul index este exclusiv (segment deschis)

# b) obțineți primele 6 caractere
s[6:]

# c) ultimele 7 caractere
s[-7:]

# d) de la indexul 12 la 19 inclusiv
s[12:19+1]

# e) tot string-ul de la coadă la cap
s[::-1]

# 2. scrieți o funcție
def count_str(txt, str, insensitive=True):
    pass
# ce numără aparițiile lui `str` în string-ul `txt`.
# testați-o cu string-ul
s = """
It was the best of times,
it was the worst of times,
it was the age of wisdom,
it was the age of foolishness,
it was the epoch of belief,
it was the epoch of incredulity,
it was the season of light,
it was the season of darkness,
it was the spring of hope,
it was the winter of despair.
"""
count_str(s, "it was")

def count_str(txt, str, insensitive=True):
    if insensitive:
        # normalizăm input-ul
        txt = txt.casefold()
        str = str.casefold()
    return txt.count(str)


# 3. scrieți o funcție
def format_seconds(total_seconds):
    """
    Converts the given seconds into a
    string of the form "[M]M:SS".
    """
    pass
# ce primind un număr întreg
# returnează un string formatat minute:secunde.
# exemplu: format_seconds(62) --> 1:02.
#
# 3.b) dacă ați terminat repede exercițiul,
# modificați funcția pentru a returna
# "[M]M:SS" sau "[H]H:MM:SS" după caz.


def format_seconds(total_seconds):
    """
    Converts the given seconds into a
    string of the form "[M]M:SS".
    """
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # if seconds < 10:
    #     seconds = "0" + str(seconds)

    # return f"{minutes}:{seconds}"

    # shorter
    return f"{minutes}:{seconds:02d}"

# even shorter
def format_seconds(total_seconds):
    """
    Converts the given seconds into a
    string of the form "[M]M:SS".
    """
    # ^^acesta se numește docstring
    # dacă în funcție primul lucru care apare este un string,
    # acesta dă documentați funcției.
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"

format_seconds(122)


# 4. folosind sintaxa de list comprehension
# și folosind `enumerate()` scrieți o funcție
def odd_elements(iterable):
    pass
# care primește ca parametru un iterabil și
# returnează o listă nouă cu elementele cu index
# impar.

def odd_elements(iterable):
    return [
        elem
        for idx, elem in enumerate(iterable)
        if idx % 2 == 1
    ]
odd_elements(range(10))


# 5. dată fiind structura de date
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
# scrieți un one-liner ce calculează media distanțelor.
#
# folosiți funcția `sum()` ce primește ca parametru un iterabil.
sum(elem[1] for elem in cities) / len(cities)

# 6. dat fiind raportul primit ca string cu acest format
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
# scrieți o funcție
def parse_report(txt):
    pass
# ce returnează o lisă de liste de forma
# [Name, Age, City].
#
# dacă scrieți o funcție intermediară
def parse_row(txt):
    pass
# puteți returna un list comprehension
# din `parse_report()`?

def parse_report(txt):
    return [
        parse_row(row)
        for row in txt.splitlines()[3:-1]
    ]

def parse_row(txt):
    return [
        item.strip()
        for item in txt[1:-1].split('|')
    ]

parse_report(s)

# 7. [opțional] scrieți o funcție
def get_seconds_from_now(timespec):
    pass
# ce returnează numărul de secunde din momentul curent
# până la următoare apariție a lui `timespec`.
#
# considerați `timespec` în format "HH:MM".
#
# sosul secret se găsește în modulul `datetime`
# în clasele `datetime` și `timedelta`.
#
# puteți folosi google, dar nu

# acum era 11:43:30. atunci, ar ieși așa:
# get_seconds_from_now('11:44') --> 30
# get_seconds_from_now('11:43') --> 24 * 60 * 60 - 30

# TODO: folosind această funcție
# creăm un script executabil
# ce să primească drept argument timespec
# și un payload (ca de exemplu să execute altă aplicație,
# sau să execute o funcție dintr-un modul de python)
#
# exemplu de comandă de shell:
# $ alarm 11:43 --payload 'mplayer alarm.mp3'
