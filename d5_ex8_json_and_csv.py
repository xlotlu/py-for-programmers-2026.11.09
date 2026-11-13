import json

# "javascript object notation"

import requests


TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(TODOS_URL)
response.content # bytes. raw response,
                 # îl folosim doar dacă luăm content binar
response.text    # bytes-ii transformați conform encoding-ului
                 # din răspunsul server-ului.
                 # este ce vrem în toate cazurile când nu avem de-a face
                 # cu raw bytes (fișiere) sau json
response.json()  # metodă ce o folosim când lucrăm cu API-uri


# scrieți o funcție
def load_todos(url, limit=10):
    pass
# ce printează titlurile primelor `limit` TODO-uri

TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

def load_todos(url, limit=10):
    response = requests.get(url)
    todos = response.json()

    for todo in todos[:limit]:
        print(todo["title"])

load_todos(TODOS_URL)

# scrieți o funcție
def save_todos(url, target_directory):
    pass
# ce salvează fiecare din todo-uri
# într-un fișier numit "<id>.json"
# în directorul target_directory


from pathlib import Path

def save_todos_to_json_files(url, target_directory):
    tdir = Path(target_directory)
    if not tdir.exists():
        tdir.mkdir()

    response = requests.get(url)
    todos = response.json()

    for todo in todos:
        # todo este un dicționar.
        # vreau să-l salvez într-un fișier cu
        fname = f"{todo['id']}.json"
        fpath = tdir / fname

        with open(fpath, 'w') as f:
            json.dump(todo, f)

# let's move these in a config module
#TODOS_URL = "https://jsonplaceholder.typicode.com/todos"
#TODOS_DIR = "the-todos"

from config import TODOS_URL, TODOS_DIR

save_todos_to_json_files(TODOS_URL, TODOS_DIR)


# working with csv
import csv
# v.1: rows are lists

with open("data/books.csv") as f:
    reader = csv.reader(f)
    for idx, row in enumerate(reader):
        print(row)
        if idx > 5: break

# v.2: rows are dicts
with open("data/books.csv") as f:
    reader = csv.DictReader(f)
    for idx, row in enumerate(reader):
        print(row)
        if idx > 5: break

# Task:
# save the TODOs that are not completed to a single csv file.
# write the following fields:
CSV_FIELDS = 'id', 'userId', 'title'#, 'completed'

def save_todos_to_csv(todos_url, csv_filename):
    response = requests.get(todos_url)
    todos = response.json()

    with open(csv_filename, 'w') as f:
        writer = csv.DictWriter(f, CSV_FIELDS,
                                extrasaction='ignore') # needed when not including all fields
        writer.writeheader()

        for todo in todos:
            if todo['completed'] is False:
                writer.writerow(todo)

save_todos_to_csv(TODOS_URL, "pending-todos.csv")
