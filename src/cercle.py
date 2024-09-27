from math import pi
from point import Point
class Cercle:
    def __init__(self, centre : Point = Point(), rayon : float = 0.0):
        """
            Méthode qui initialise une instance de Cercle
        :param c: Point central du cercle utilisant la class Point()
        :param r: rayon
        """
        self.__c = centre
        self.__r = rayon

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
    def r(self):
        return self.__r

    @r.setter
    def r(self, val):
        if isinstance(val, float):
            self.__r = val
        else:
            raise ValueError("r n'est pas un réel")

    def diametre(self) -> float:
        """
            Méthode qui calcul le diamètre du cercle
        :return: diamètre
        """
        return self.__r*2

    def perimetre(self) -> float:
        """
            Méthode qui calcul le périmètre du cercle
        :return: périmètre
        """
        return 2*pi*self.__r
    def surface(self) -> float:
        """
            Méthode qui calcul la surface du cercle
        :return: surface
        """
        return pi*self.__r**2
    def intersection(self, camarade) -> bool:
        """
            Méthode qui vérifie si le cercle croise un autre
        :return: VRAI = Il y a une intersection, FAUX = Il n'y a pas d'intersection
        """
        d = self.__c.distancePoint(camarade.__c)
        if d - self.__r - camarade.__r <= 0:
            return True
        else:
            return False
    def point(self, a : float, b : float) -> bool:
        """
            Méthode qui vérifie si le point de coordonnées (a,b) fait parti du cercle
        :param a: x valeur de coordonné en abscisse du point
        :param b: y valeur de coordonné en ordonnée du point
        :return: VRAI = Le point est dans le cercle, FAUX = Le point n'est pas dans le cercle
        """
        d = self.__c.distancePoint(Point(a,b))
        if d - self.__r <= 0:
            return True
        else:
            return False

def principale():
    C = Cercle(Point(6.5,2.5),1.5)
    D = Cercle(Point(10,1),3)
    print(C.intersection(D))

    E = Cercle(Point(16.5, 1), 6.5)
    print(C.point(16,4))

if __name__=='__main__':
    principale()