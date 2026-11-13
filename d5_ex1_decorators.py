# un decorator este un callable
# ce primește ca argument un callable
# și returnează un alt callable

# callable = o funcție, o clasă, sau un obiect
#             ce poate fi "executat"


# Task:
# scrieți un decorator ce cronometrează
# execuția funcțiilor pe care le decorează
# și face print cu numele funcției, argumentele sale
# și timpul de execuție


from datetime import datetime

def timeit(func):
    print("! inițializare decorare a lui", func)
    # ca de exemplu, ne creăm aici un cache
    # specific pentru `func`.

    LOG_TEMPLATE = "» {module}.{name}({args}) --> {result} :: {time}ms"

    def _inner(*args, **kwargs):
        # aici suntem în funcția modificată.
        # putem face lucruri înainte de
        # a o executa pe cea originală

        print("» începem măsurare")
        start_time = datetime.now()

        retval = func(*args, **kwargs)

        # și putem face lucruri înainte de
        # a returna rezultatul execuției
        end_time = datetime.now()

        delta = end_time - start_time

        log_args = map(repr, args)

        print(
            LOG_TEMPLATE.format(
                module=func.__module__,
                name=func.__name__,
                args=", ".join(log_args),
                result=repr(retval),
                time=delta.total_seconds() * 1000
            )
        )

        print("» am încheiat timing")

        return retval

    print("! încheiat procedură de inițializare")

    return _inner

from time import sleep

#@timeit
def myfunc(x, y, z):
    sleep(x / 10)
    return f"îți returnez ceva pentru {x}"
#myfunc = timeit(myfunc)
#print(
#    "myfunc returnează:",
#    myfunc(5, 6, "bla")
#)
myfunc = timeit(myfunc)

from functools import cache
from random import randint

@timeit
@cache
def sleepy(x, y):
    sleep(randint(x, y) / 10)
    return "i slept so well"
#sleepy = timeit(cache(sleepy))

#sleepy(4, 10)
