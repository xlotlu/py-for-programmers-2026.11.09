# un context manager este introdus cu statement-ul `with`
# și garantează că la intrarea și ieșirea în/din
# ctx manager, se rulează cod specific.
#
# ce înseamna aceasta ("cod specific") este dictat
# de context manager în sine.

# exemplu 1:
with open("orar.txt") as f:
    # garantează că se rulează f.close()
    pass

# exemplu 2: ctx manager-ul lui sqlite:
import sqlite3

con = sqlite3.connect("my.db")
con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

# con funcționează și ca context manager,
# garantând rollback() sau commit()
# în funcție de succesul operațiunilor

try:
    with con:
        con.execute("INSERT INTO lang(name) VALUES('Python')")
        con.execute("INSERT INTO lang(name) VALUES('Rust')")
        1 / 0
except ZeroDivisionError:
    print("a fost o eroare de la noi, nu de la db")

for elem in con.execute("SELECT * from lang"):
    print(elem)
# nici-un rezultat, pentru că
# context manager-ul `con` a făcut auto-rollback

# vs.
with con:
    con.execute("INSERT INTO lang(name) VALUES('Python')")
    con.execute("INSERT INTO lang(name) VALUES('Rust')")
# la ieșire, context manager-ul a făcut auto-commit
for elem in con.execute("SELECT * from lang"):
    print(elem)
