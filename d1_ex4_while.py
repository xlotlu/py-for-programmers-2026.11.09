while condition:
    statements

    break       # oprește execuția buclei
    continue    # continuă cu iterația următoare buclei
                # (adică orice cod scris mai jos de continue
                # nu se va mai executa în bucla curentă)

# Task:
# numărați în ordine inversă de la 5 la 0,
# și faceți print fiecărui număr.

x = 5
while x >= 0:
    print(x)
    #x = x - 1
    # echivalent cu
    x -= 1

# cealaltă modalitate:
x = 5
while True:
    # ne asigurăm în interior
    # că ieșim din buclă cu un break
    # (sau cu return dacă suntem în interiorul unei funcții)
    print(x)
    x -= 1

    if x >= 0:
        continue
    else:
        break

x = 5
while True:
    print(x)

    x -= 1

    if x < 0:
        break

# Task:
# scrieți o funcție
def prompt_for_int():
    pass

# ce promptează utilizatorul pentru un număr întreg
# și îl returnează drept int.
#
# strategie:
# 0. intrăm într-o buclă infinită
# 1. cerem utilizatorului un număr
# 2. verificăm dacă string-ul este decimal, cu .isdecimal()
# 3. dacă da, return
# 4. dacă nu, spune-i utilizatorului că eroare

def prompt_for_int():
    while True:
        num = input("Introdu un numar intreg: ")
        if num.isdecimal():
            return int(num)
        else:
            print("Nu ai introdus un numar intreg. Mai incearca.")

prompt_for_int()

# v.2. cu try / except

def prompt_for_int():
    while True:
        num = input("Introdu un numar intreg: ")

        try:
            return int(num)
        except ValueError:
            print("Număr invalid.")


# Modificăm funcția de mai sus
# pentru a primi un argument `prompt` opțional
# ce va fi pasat mai departe funcției input.

def prompt_for_int(prompt="Introdu un numar intreg: "):
    while True:
        num = input(prompt)

        try:
            return int(num)
        except ValueError:
            print("Număr invalid.")


# Scrieți o funcție
def test_for_age():
    pass
# ce promptează utilizatorul să își scrie vârsta,
# și apoi dacă este între 18 și 60 de ani,
# îi scrieți că este acceptat, altfel refuzat.
#
# folosiți în interiorul acestei funcții pe prompt_for_int().

def test_for_age():
    age = prompt_for_int("Care este vârsta ta? ")

    if 18 <= age <= 60:
        print("Acceptat")
    else:
        print("Ne-acceptat")
