from functools import cache

# dataset-ul:
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# we want cached retrieval
@cache
def get_friend_by_name(name):
    print("» looking up:", name)
    for friend in friends:
        if friend[0] == name:
            return friend


from random import randint

def myrand(a, b):
    return randint(a, b)
myrand(1, 100)
myrand(1, 100) # different value

# vs.
@cache
def myrand(a, b):
    return randint(a, b)
myrand(1, 100)
myrand(1, 100) # same value
myrand(1, 101) # different value
myrand(1, 101) # same value


# un decorator este o funcție
# care primește ca argument o funcție
# și returnează o altă funcție

# dat fiind
def myrand(a, b):
    return randint(a, b)

# aceasta este o funcție nouă
# (mi-am decorat o funcție cu new behaviour)
mycached_rand = cache(myrand)

# dar dacă aș face...
myrand = cache(myrand)

# este perfect echivalent cu:
@cache
def myrand(a, b):
    return randint(a, b)

# deci sintaxa cu @decorator înaintea funcției
# este syntactic sugar în jurul lui
# myfunc = decorator(myfunc)

# acesta este un decorator care nu face nimic special
def mydeco(func):
    def _inner(*args, **kwargs):
        # fac ceva la intro
        print("running", func, "with", args)

        retval = func(*args, **kwargs)

        # fac ceva la outro
        print("which returned", retval)

        return retval
    return _inner

@mydeco
def myrand(a, b):
    return randint(a, b)
