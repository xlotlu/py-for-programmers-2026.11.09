# scrieți o funcție
def read_contents(filename):
    pass
# ce returnează conținutul fișierului `filename`

# scrieți o funcție
def write_contents(filename, content):
    pass
# ce scrie string-ul `content` în fișierul `filename`


def read_contents(filename):
    with open(filename) as f:
        return f.read()

def write_contents(filename, content, overwrite=False):
    # folosim modul care refuză să facă overwrite
    mode = 'w' if overwrite else 'x'

    with open(filename, mode) as f:
        f.write(content)


# știind că obiectele file pointer sunt iterabile
# linie cu linie, scrieți o funcție
def grep(filename, match, insensitivae=False):
    pass
# ce printează toate liniile din fișierul `filename`
# care conțin substring-ul `match`

# testați cu
grep("concepts-cheatsheet-notes.md", "Python")


def grep(filename, match, insensitive=False):
    if insensitive:
        match = match.casefold()

    with open(filename) as f:
        for line in f:
            _line = line.casefold() if insensitive else line

            if match in _line:
                print(line.removesuffix("\n"))

# Scriem o funcție
def cp(infile, outfile):
    "copies the contents of `infile` to `outfile`"

    with open(infile) as f_in:
        with open(outfile, 'w') as f_out:
            # totul intră în memorie!
            # în plus, stă să aștepte până începe să scrie
            f_out.write(
                f_in.read()
            )
# v. alternativă:
def cp(infile, outfile):
    "copies the contents of `infile` to `outfile`"

    with open(infile) as f_in:
        with open(outfile, 'w') as f_out:
            for line in f_in:
                f_out.write(line)

# rescris cu un singur `with` statement:
def cp(infile, outfile):
    "copies the contents of `infile` to `outfile`"

    # \ la sfârșitul liniei este "line continuation character"
    with open(infile) as f_in, \
         open(outfile, 'w') as f_out:
        for line in f_in:
            f_out.write(line)

# sau:
def cp(infile, outfile):
    "copies the contents of `infile` to `outfile`"

    with (
        open(infile) as f_in,
        open(outfile, 'w') as f_out
    ):
        for line in f_in:
            f_out.write(line)

# notă 1: acesta nu va merge pe fișiere binare
# notă 2: pentru că este default mode text, care
#         face conversie de encoding

# Exercițiu:
# scrieți o funcție
def strip_comments(infile, outfile):
    pass
# ce scrie în `outfile` conținutul lui `infile`
# cu toate liniile care încep cu '#' ignorate.


def strip_comments(infile, outfile):
    with (
        open(infile) as f_in,
        open(outfile, 'w') as f_out
    ):
        for line in f_in:
            if not line.startswith("#"):
                f_out.write(line)

# alternativ, cu `.writelines()` ce scrie
# un iterabil gata filtrat
def strip_comments(infile, outfile):
    with (
        open(infile) as f_in,
        open(outfile, 'w') as f_out
    ):
        # implicație:
        # întrucât:
        #   1) `filter()` returnează un iterator
        #   și 2) `f_in` este iterabil...
        # întregul flux de date este în continuare line-by-line
        f_out.writelines(
            filter(lambda line: not line.startswith("#"),
                   f_in)
        )

# sau și mai citabil cu generator expression:
def strip_comments(infile, outfile):
    with (
        open(infile) as f_in,
        open(outfile, 'w') as f_out
    ):
        f_out.writelines(
            line
            for line in f_in
            if not line.startswith("#")
        )

strip_comments("d4_ex3_working_with_files.py", "my_copy.py")

# remember: encoding was system-dependent before Python 3.15.
# this means Windows defaults were not compatible with
# Linux/Mac defaults. if you want interoperabilty
# (or if you want diacrtics or any special character),
# always add `encoding="utf-8"`:
with open("test.txt", 'w', encoding="utf-8") as f:
    f.write('Şi atunci am sărit pe şa. Ţaţaţa în pe undâva.')

import io

# revizităm `def cp()` pentru fișiere binare:
def cp(infile, outfile, chunk_size=io.DEFAULT_BUFFER_SIZE):
    "copies the contents of `infile` to `outfile`"

    with (
        open(infile, 'rb') as f_in,
        open(outfile, 'wb') as f_out
    ):
        while True:
            chunk = f_in.read(chunk_size)
            if not chunk:
                break
            f_out.write(chunk)

# nu ar fi frumos să avem while direct pe chunk?
def cp(infile, outfile, chunk_size=io.DEFAULT_BUFFER_SIZE):
    "copies the contents of `infile` to `outfile`"

    with (
        open(infile, 'rb') as f_in,
        open(outfile, 'wb') as f_out
    ):
        # "the walrus operator": assignment within statements
        while chunk := f_in.read(chunk_size):
            f_out.write(chunk)
