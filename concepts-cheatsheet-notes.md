# concepts

în Python totul(!) este un obiect
in Python totul(!) este o referință

reprezentare: felul în care obiectul este afișat
              în context de development

Python is dynamically typed
(putem re-asigna variabila la alte data-type-uri)

iteratorii: sunt iterabili
            nu au nevoie să fie memory-backed
            sunt suspendați în execuție
            iterația îi deblochează
            și suportă funcția next()

Python is "self-documenting"


# things to read

(at least once in a Python programmer's lifetime)

The Styleguide:
https://peps.python.org/pep-0008/

```python
import this
```


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
type() # returnează clasa din care a fost instanțiat obiectul


# important exceptions:

NameError       simbolul respectiv (variabila) nu este definit(ă)
ValueError      apare când valoarea trimisă unei funcții
                este invalidă. (context-dependent)
TypeError       call invalid de funcții și
                operațiuni cu tipuri incompatibile
AttributeError  atributul respectiv nu există
IndexError      indexul respectiv nu există
KeyError        cheia respectivă nu există


# useful and very useful packages

pachetele se instalează cu comanda de shell de sistem:

(adică în cmd sau powershell)

```shell
pip install package_name
```

* `ipython`: shell superb de python, cu comenzi interne specializate
  și syntax highlighting și auto-completion
* `rich`: aduce multe modalități de formatare și syntax highlighting
  al codului, structurilor de date și excepțiilor. poate fi integrat
  ușor cu (i)python:
  
  ```python
  from rich import pretty
  pretty.install() # makes object representations pretty
  # override the default print:
  from rich import print
  ```

## for accelerating code:

* numba: first line of defense
* cython: if you want compiled C modules

## for real-world scenarios:

* requests: de-facto standard for http work
* flask: web micro-framwork
* django: monolithic, full-featured web framework
  that does excellent data modelling
* pydantic: framework for data modelling, processing
  and(!) validation
* fastapi: framework for creating REST APIs,
  based on pydantic


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
