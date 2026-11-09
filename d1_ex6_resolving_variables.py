x = 15

def func():
    # aici nu există o variabilă locală `x`
    # deci va încerca să o rezolve dintre
    # variabilele globale.
    print(x)

func() # printează 15


def func(x):
    print(x)

func(12)


x = 15
def func():
    x = x + 1
    print(x)

#func() # --> UnboundLocalError exception

lst = []
def func():
    lst.append("something")
    print(lst)



# dacă **CHIAR** vrem să operăm
# asupra unei variabile globale:
x = 15
def func():
    global x
    # ^^ valabil doar în interiorul aceste funcții
    x = x + 1
    print(x)
# please don't do this:
# - it results in spaghetti code
# - it is *exponentially* prone to bugs
# - every time you do this a baby seal cries

# statement-ul care compensează pe global
# în cazul funcțiilor definite în funcție:
x = 15
def myfunc():
    x = 17
    def otherfunc():
        nonlocal x
        x += 1
        print("inner says:", x)
    otherfunc()
    otherfunc()
    otherfunc()
    print("outer says:", x)
myfunc()

# devine util pentru closure-uri:
def function_factory():
    x = 17

    def otherfunc():
        nonlocal x
        x += 1
        print("inner says:", x)

    return otherfunc

myfunc = function_factory()
myfunc() # prints 18
myfunc() # prints 19
