import random

class MyClass:
    @property
    def my_attr(self):
        return random.randint(1, 10)

obj = MyClass()
obj.my_attr
obj.my_attr

# 1. @property
# permite implementare de getter / setter ( / deleter)

class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Account balance cannot be negative")
        self._balance = value


# 2. @staticmethod
# utilitate:
# o funcție utilitară ce are sens împreună cu clasa respectivă.

# în loc să facem
def add(a, b):
    print(a, b)
    return a + b

class MyClass:
    def __init__(self):
        self.x = 0
        self.y = 0

# lipim funcția utilitară în namespace-ul clasei
class MyClass:
    def __init__(self):
        self.x = 0
        self.y = 0

    @staticmethod
    def add(a, b):
        print(a, b)
        return a + b


# 3. @classmethod
# utilitate 1: factory method
# utilitate 2: exact ca staticmethod (o funcție utilitară)
#              doar că are nevoie să știe care îi este clasa.
#              (pentru a își modifica behavior-ul în funcție de
#               specificitățile claseo)

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)


class Parent:
    ATTR = "parent attr" # class-level attribute

    @classmethod
    def get_the_attr(cls):
        return cls.ATTR

class Child(Parent):
    ATTR = "child attr"


# o notă despre class-level attributes:
obj1, obj2, obj3 = Parent(), Parent(), Parent()
obj1.ATTR, obj2.ATTR, obj3.ATTR
# pointere către același obiect:
# ('parent attr', 'parent attr', 'parent attr')

obj1.ATTR = "o valoare"
# am schimbat pointer-ul acestui obiect:
obj1.ATTR, obj2.ATTR, obj3.ATTR
# ('o valoare', 'parent attr', 'parent attr')

Parent.ATTR = "l-am schimbat"
# am schimbat valoarea atributului pe clasă
obj1.ATTR, obj2.ATTR, obj3.ATTR
# ('o valoare', 'l-am schimbat', 'l-am schimbat')