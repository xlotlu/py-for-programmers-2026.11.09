# dat fiind string-ul
s = "O zi minunată cu soare cu dințișori"

# des folosite
s.lower()
s.upper()

s.replace("u", "oo")

s.split()
# ^^ split după orice whitespace
#    în timp ce înghite whitespace-uri multiple

"""
un string multi-line
cu spații și \t tab
""".split()

# vs.
" un string    cu multe spații   ".split(" ")
# care adaugă elemente goale

"|".join(lst)


"    un string    cu multe spații   ".strip()
"    un string    cu multe spații   \n".strip()
# vs.
"    un string    cu multe spații   \n".strip(" ")
"    un string    cu multe spații   \n".strip(" \n")


# task:
# să obținem int din:
num = "0001230"
int(num.lstrip("0"))


# mai rar folosite

s.startswith("O")
s.endswith("ri")

s1 = "» Aceasta este o linie\n"
s2 = "Aceasta este o linie"
(
    s1.removeprefix("» ").removesuffix("\n")
    ==
    s2.removeprefix("» ").removesuffix("\n")
)



s.isdecimal()

s.casefold()
# există pentru că...
'ß'.lower() != 'ß'.casefold()
'σ' == 'ς'.casefold()

s1 = "STRASSE"
s2 = "Straße"
s1.lower() != s2.lower()
s1.casefold() == s2.casefold()

# ^^  deci este folosit doar în algoritmi de case-insensitive string comparison


# dacă aveți de splitat un text după linii:
s = 'un text\r\nscris pe windows\r\n'
s.splitlines()

# poate:
column = "Home Address"
column.center(50, '=')
column.rjust(50, '=')

table = str.maketrans("abcd", "ABCD") # este un classmethod
s.translate(table) # face multiple replace-uri 1:1


# Exercițiu
# dat fiind capul de tabel dintr-un raport text antic:
header = "|   Name   |   Home Address  |    Phone    |"
# extrageți numele coloanelor într-o listă

# split după "|"
# eliminăm obiectele goale
# strip pe ce rămâne

_columns = header.split("|")
columns = []
for item in _columns:
    if item == '':
        continue
    columns.append(item.strip())
print(columns)

# cu strip inițial
columns = []
for col in header.strip("|").split("|"):
    columns.append(col.strip())
