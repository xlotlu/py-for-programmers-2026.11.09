# pe vremuri, cu fișiere lucram așa:

f = open("orar.txt")

try:
    # operațiuni cu f
    # și alte operațiuni
    pass
finally: # acesta se execută întotdeauna
    f.close()

# zilele acestea facem:
with open("orar.txt") as f:
    # operațiuni
    pass
# în cazul de sus, context manager-ul se ocupă
# să facă .close()


# sintaxa completă de exception handling
try:
    # statements care pot cauza excepție
    pass
except IndexError as e:
    # facem handling doar de IndexError
    # și în acest avem acces la excepție
    print(e)
    pass
except ValueError:
    # facem handling doar de ValueError
    pass
# ....
except: # catch-all
    pass
finally:
    # se rulează în toate cazurile
    pass

# exemplu de ce este else util:
# dacă am vrea să rulăm cod condițional
# *doar* dacă nu a fost eroare (care altfel ar fi fost handled)
errors = True
try:
    1 / 1
    errors = False
except ZeroDivisionError:
    print("a fost 0")
if not errors: print("good stuff")
# este echivalent cu
try:
    1 / 1
except ZeroDivisionError:
    print("a fost 0")
else:
    print("good stuff")


# variațiunile sunt:
try:
    pass
#except Type1:
#    pass
#except Type2:
#    pass
except: # / except Exception: / except Exception as e:
    pass

try:
    pass
finally:
    pass

try:
    pass
# except ...
except:
    pass
else:
    pass


try:
    pass
# except ...
except:
    pass
else:
    pass
finally:
    pass


#raise ExceptionType("exception message")

# și o notă despre raise:
# fără argumente raise-uiește excepția curentă
try:
    1 / 0
except:
    print("am prins-o")
    raise # raise-uiește excepția curentă
