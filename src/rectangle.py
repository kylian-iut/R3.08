from typing import List

from point import Point
from src.point import Point


class Rectangle:
    def __init__(self, point_initial: Point = Point(), longueur: float = 1.0, hauteur: float = 1.0):
        """
            Méthode qui initialise une instance de Rectangle
        :param point_initial: Point initial en bas à gauche du rectangle
        :param longueur: longueur parallèle à l’axe des abscisses
        :param hauteur:  hauteur parallèle à l’axe des ordonnées
        """
        self.__p = point_initial
        self.__l = longueur
        self.__h = hauteur

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, val):
        if isinstance(val, Point):
            self.__p = val
        else:
            raise ValueError("p n'est pas un point")

    @property
    def l(self):
        return self.__l

    @l.setter
    def l(self, val):
        if isinstance(val, float):
            self.__l = val
        else:
            raise ValueError("l n'est pas un réel")

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, val):
        if isinstance(val, float):
            self.__h = val
        else:
            raise ValueError("h n'est pas un réel")

    def surface(self) -> float:
        """
            Méthode qui permet de calculer la surface du Rectangle
        :return: Surface
        """
        return self.__l * self.__h

    def perimetre(self) -> float:
        """
        Méthode qui permet de calculer le périmètre du Rectangle
        :return: Périmètre
        """
        return 2 * (self.__h + self.__l)

    def points(self) -> list[Point]:
        """
            Méthode qui renvoie la liste des quatres Points du rectangle
        :return: [Point supérieur gauche, Point supérieur droit, Point inférieur gauche, Point inférieur droit]
        """
        sg = Point(self.__p.x, self.__p.y + self.__h)
        sd = Point(self.__p.x + self.__l, self.__p.y + self.__h)
        ig = self.__p
        id = Point(self.__p.x + self.__l, self.__p.y)
        ls = []
        for co in [sg,sd,ig,id]:
            ls.append([co.x,co.y])
        return ls

    def point(self, point : Point = Point()) -> bool:
        """
            Méthode qui vérifie si un Point se trouve dans le Rectangle
        :return: True = le Point est dans le rectangle, False = le Point n'est pas dans le rectangle
        """
        if self.__p.x <= point.x and point.x <= self.__p.x + self.__l and self.__p.y <= point.y and point.y <= self.__p.y + self.__h:
            return True
        else:
            return False

def principale():
    C = Rectangle(Point(-1,1),6,4.2)
    print(C.points())
    print(C.point(Point(1.6,2.5)))

if __name__=='__main__':
    principale()