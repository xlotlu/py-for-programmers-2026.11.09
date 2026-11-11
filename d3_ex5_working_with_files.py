with open("orar.txt") as f:
    print(f.read())

# modes:
# default: 'r'
with open("orar.txt", 'r') as f:
    print(f.read())

# 'w' creates the file, truncates it unconditionally
with open("newfile.txt", 'w') as f:
    f.write("don't overwrite me please!\n")
    f.write("I can write in files, weee\n")
    f.write("I can even write some more!")

# 'x' creates the file, refuses to overwrite:
with open("newfile.txt", 'x') as f:
    f.write("don't overwrite me please!\n")


# "with" introduce un "context manager"
# -- în cazul lui open() se asigură că face singur .close()
