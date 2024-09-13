from math import sqrt


class Point:
    def __init__(self, a=0.0, b=0.0):
        """
            Méthode qui permet d'initialiser un point et ses coordonnées
        :param a: x (abscisse)
        :param b: y (ordonnée)
        """
        self.__x = a
        self.__y = b

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if isinstance(val, float):
            self.__x = val
        else:
            raise ValueError("x n'est pas un réel")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if isinstance(val, float):
            self.__y = val
        else:
            raise ValueError("y n'est pas un réel")

    def distanceCoord(self, a: float, b: float):
        """
            Méthode qui calcul la distance entre le point et des coordonnées
        :param a: x (abscisse)
        :param b: y (ordonnée)
        :return: float
        """
        return sqrt((self.y - b) ** 2 + (self.x - a) ** 2)

    def distancePoint(self, camarade):
        """
            Méthode qui calcul la distance entre deux points
        :param camarade: Point
        :return: float
        """
        return sqrt((self.y - camarade.y) ** 2 + (self.x - camarade.x) ** 2)

def principale():
    A = Point()
    B = Point(5.5, 6.6)
    print(A.distancePoint(B))

if __name__=='__main__':
    principale()