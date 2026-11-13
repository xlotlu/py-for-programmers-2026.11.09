# în Python există multiple inheritance:

# this can cause "diamond-inheritance"

class Ancestor:
    def method(self):
        print("Ancestor method")

class Parent1(Ancestor):
    def method(self):
        Ancestor.method(self)
        print("Parent 1 method()")

class Parent2(Ancestor):
    def method(self):
        Ancestor.method(self)
        print("Parent 2 method()")

class Child(Parent1, Parent2):
    def method(self):
        Parent2.method(self)
        Parent1.method(self)
        print("Child method()")

print("=== diamond 1 ===")
obj = Child()
obj.method()

print("\n")

# introducing:
# super()

class Ancestor:
    def method(self):
        print("Ancestor method")

class Parent1(Ancestor):
    def method(self):
        super().method()
        print("Parent 1 method()")

class Parent2(Ancestor):
    def method(self):
        super().method()
        print("Parent 2 method()")

class Child(Parent1, Parent2):
    def method(self):
        super().method()
        print("Child method()")

print("=== diamond 2 ===")
obj = Child()
obj.method()

# explicație:
# magia pe care o face super
# este să acceseze atributele (adică și metodele)
# obiectului curent, în contextul clasei părinte / claselor părinte


### class-based iterators:
# 1. trebuie să poată fi transformat în iterator

class MyIterable:
    def __iter__(self):
        return self

    def __next__(self):
        return "something"
