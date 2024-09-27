from math import sqrt
from point import Point


class Triangle:
    def __init__(self, cote_droit: Point = Point(), adjacent: float = 1.0, opposee: float = 1.0):
        """
            Méthode qui initialise une instance de Triangle rectangle
        :param cote_droit: Point du côté droit du triangle rectangle
        :param adjascent: longueur du côté adjacent
        :param opposee:  longeur du côté opposé
        """
        self.__c = cote_droit
        self.__a = adjacent
        self.__o = opposee

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if isinstance(val, Point):
            self.__c = val
        else:
            raise ValueError("c n'est pas un point")

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        if isinstance(val, float):
            self.__a = val
        else:
            raise ValueError("a n'est pas un réel")

    @property
    def o(self):
        return self.__o

    @o.setter
    def o(self, val):
        if isinstance(val, float):
            self.__o = val
        else:
            raise ValueError("o n'est pas un réel")

    def hypothenuse(self) -> float:
        """
            Méthode qui calcul l'hypothénuse du triangle rectangle
        :return: hypothénuse
        """
        return sqrt(self.__o**2+self.__a**2)

    def perimetre(self) -> float:
        """
            Méthode qui calcul le périmètre du triangle
        :return: périmètre
        """
        return self.hypothenuse() + self.__a + self.__o

    def surface(self) -> float:
        """
            Méthode qui calcul la surface du triangle
        :return: surface
        """
        return self.__o * self.__a / 2

    def isocele(self) -> bool:
        """
            Méthode qui vérifie sur le triangle est isocèle
        :return: True = le triangle est isocèle, False = le triangle n'est pas isocèle
        """
        if self.__a == self.__o:
            return True
        else:
            return False


def principale():
    C = Triangle(Point(-1, 1), 6, 6)
    print(C.isocele())
    print(C.surface())
    print(C.hypothenuse())
    print(C.perimetre())


if __name__ == '__main__':
    principale()
