# generators are functions that yield values repeteadly
# instead of returning (once).

from time import sleep
def mygen():
    print("am intrat în funcție")

    yield "prima valoare"
    sleep(3)
    print("continui 1")

    yield "a doua valoare"
    sleep(3)
    print("continui 2")

    yield "a treia valoare"
    sleep(3)
    print("am ieșit din funcție")

# generatorul este un caz particular de iterator.
# el se suspendă în execuție după fiecare yield


def squares(iterable):
    for elem in iterable:
        yield elem ** 2
        sleep(1)

# let's filter books by genre
# without loading everything in memory
def filter_books_by_genre(books, genre):
    for book in books:
        if book['Genre'] == genre:
            yield book

import csv
with open("data/books.csv") as f:
    reader = csv.DictReader(f)
    for book in filter_books_by_genre(reader, 'data_science'):
        print(book)
