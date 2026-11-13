# argumente poziționale
def func(a, b):
    print("» a", a)
    print("» b", b)

func(1, 2)

# funcție care primește
# oricâte argumente poziționale
def func(a, b, *args):
    # *args se numește "argument packing"
    print("» a", a)
    print("» b", b)
    print("» args", args)

func(1, 2, 3, 4)

# primește și keyword-arguments
def func(a, b, *args, kw1="un default", kw2="doi default"):
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kw1", kw1)
    print("» kw2", kw2)

func(1, 2, 3, 4)
func(1, 2, 3, 4, kw2="something else")

# funcție care primește oricâte kwargs
def func(a, b, *args, kw1="un default", kw2="doi default", **kwargs):
    # **kwargs se numește "keyword-argument packing"
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kw1", kw1)
    print("» kw2", kw2)
    print("» kwargs", kwargs)

func(1, 2, 3, 4)
func(1, 2, 3, 4, something="wow", etc="wow again")

# există și argument unpacking:
lst = [1, 2, 3, 4]
func(*lst) # am despachetat iterabilul drept argumente

# și kwarg unpacking:
kargs = {"kw1": "arg diferit", "arg1": "v1", "arg2": "v2"}
func(*lst, **kargs)

opts = {
    'sep': '  ||  ',
    'end': '«««\n',
}

print("ala", "bala", "porto", **opts)
# echivalent cu
print("ala", "bala", "porto", sep='  ||  ', end='«««\n')


# notă. remember iterable unpacking?
a, b, c = range(3)
# putem captura și elemente în plus
# față de variabilele date:
a, b, c, *rest = range(5)
*rest, a, b, c = range(5)
a, b, *rest, c = range(5)


# a forța ca unele argumente să fie
# ori poziționale, ori keywords
def func(a, b):
    pass

func(1, 2) # merge
func(1, b=2) # merge
func(b=2, a=1) # merge

# * spune: de aici încolo
#          doar keyword arguments
def func(a, *, b=None):
    pass
func(1, 2)  # --> TypeError
func(1, b=2) # merge
func(a=1, b=2) # merge

# / spune: până aici
#          doar poziționale
def func(a, /, b=None):
    pass

func(1, 2) # merge
func(1, b=2) # merge
func(a=1, b=2) # --> TypeError
