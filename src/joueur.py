from personnage import Personnage

class Joueur:
    def __init__(self, nom : str, n_max_person : int):
        """
            Méthode qui initialise une instance de Joueur
        :param nom:  Nom du joueur
        :param n_max_person: Quantité maximal de personnage
        """
        self.__nom = nom
        self.__max = n_max_person
        self.__perso = []

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, val):
        if isinstance(val, str):
            self.__nom = val
        else:
            raise ValueError("nom n'est pas une chaine")

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, val):
        if isinstance(val, int):
            if val >= 1:
                self.__max = val
            else:
                self.__max = 1
        else:
            raise ValueError("max n'est pas un entier")

    @property
    def perso(self):
        return self.__n

    @perso.setter
    def perso(self, val):
        if isinstance(val, list(Personnage)):
            if val >= 0:
                self.__n = val
            else:
                self.__n = 0
        else:
            raise ValueError("n n'est pas un entier")