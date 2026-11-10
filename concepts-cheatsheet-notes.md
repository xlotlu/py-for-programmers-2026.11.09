TODO.

# concepts

în Python totul(!) este un obiect
in Python everything(!) este o referință


reprezentare: TODO

Python is dynamically typed
(putem re-asigna variabile la alte data-type-uri)


iteratorii: sunt iterabili
            nu au nevoie să fie memory-backed
            sunt suspendați în execuție
            iterația îi deblochează
            și suportă funcția next()



# things to read

(at least once in a Python programmer's lifetime)

The Styleguide:
https://peps.python.org/pep-0008/


# operators

//     partea întreagă a împărțirii
%      restul împărțirii
**     ridicare la putere

## boolean:

and
or
not

in
not in

is
is not


# basic data types

int
float
str

bool

tuple  # immutable
list   # mutable

## sequences

str, tuple, list:

- sunt iterabile
- sunt accesibile după index
- au o lungime dată
  (accesibilă cu funcția `len()`)
- suportă operatorul `in`
- au metodele `.count()` și `.index()`



# debugging essentials

print()
help()
type()

# important exceptions:

ValueError      apare când valoarea trimisă unei funcții
                este invalidă. (context-dependent)
AttributeError


# working with VSCode:

Ctrl+F5     run file in Python
Shift+Enter run selection (or current line)
Ctrl+/      comment selection (or current line)
Tab         indent selection
Shift+Tab   unindent selection


# varia

There are 2 most difficult problems in computing:
- naming things
- cache invalidation
- off-by-one errors
