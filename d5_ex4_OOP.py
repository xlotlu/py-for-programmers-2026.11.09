# un obiect este o instanță a unei clase
# P.S.: în Python totul este un obiect.

class MyClass:
    # metodele primesc automat ca prim argument
    # obiectul curent
    def method(this, x, y):
        print(this)
        return x + y

class MyClass:
    # metoda __init__ dă semnătura clasei.
    # și este procedura de inițializare a obiectului.
    # deci nu constructor. obiectul a fost deja construit.
    def __init__(self, x):
        print(self)
        self.x = x


# există double-underscore methods speciale,
# documentate, care fac tot ce am văzut până acum.
# sunt prescurtate "dunder" methods & attributes

import math

class Point:
    """
    A two-dimensional point.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property # are sens doar în context de clasă
    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

# Exercițiu:
# Scrieți o clasă
class ThreeDPoint:
    pass
# ce implementează un punct 3D cu aceleași
# metode ca mai sus.

# în loc de a da copy-paste
class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

# vreau să las părintele să își facă treaba
class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)

        self.z = z

    def translate(self, dx, dy, dz):
        Point.translate(self, dx, dy)

        self.z += dz

# ok, în clipa asta funcționalitatea este ok,
# dar restul metodelor sunt tot configurate pe 2d.
#
# aș vrea o abstractizare să nu rescriu
# manual pe __repr__, __str__, __eq__

class Point:
    """
    A two-dimensional point.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}{self.coordinates}"

    def __str__(self):
        return str(self.coordinates)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        #print("verifying if equal")
        return self.coordinates == other.coordinates

    def __lt__(self, other):
        #print("verifying if less")
        return self.coordinates < other.coordinates

    @property
    def distance_from_origin(self):
        return math.sqrt(
            sum(
                coord ** 2 for coord in self.coordinates
            )
        )

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)

        self.z = z

    @property
    def coordinates(self):
        return self.x, self.y, self.z

    def translate(self, dx, dy, dz):
        Point.translate(self, dx, dy)

        self.z += dz


# finally, add substraction
# and make distance_from_origin generic as well
# by using a staticmethod

class Point:
    """
    A two-dimensional point.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}{self.coordinates}"

    def __str__(self):
        return str(self.coordinates)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        #print("verifying if equal")
        return self.coordinates == other.coordinates

    def __lt__(self, other):
        #print("verifying if less")
        return self.coordinates < other.coordinates

    def __sub__(self, other):
        dist = self.compute_distance(self.coordinates, other.coordinates)

        return f"returning Vector(dist={dist}, angle=something)"

    @property
    def distance_from_origin(self):
        return self.compute_distance(self.coordinates)

    @staticmethod
    def compute_distance(A, B=None):
        """
        computes the distance between points `A` and `B`.
        the points must be expressed as equal-length iterables.
        if `B` is `None`, compute the distance to origin.
        """
        if B is None:
            # simplify the expression below by creating B anyway
            B = (0,) * len(A)

        return math.sqrt(sum(
            (c2 - c1) ** 2
            for c1, c2 in zip(A, B, strict=True)
        ))

# also, switch to using super()

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)

        self.z = z

    @property
    def coordinates(self):
        return self.x, self.y, self.z

    def translate(self, dx, dy, dz):
        super().translate(dx, dy)

        self.z += dz


print(Point(3, 4).distance_from_origin)
print(ThreeDPoint(2, 3, 6).distance_from_origin)