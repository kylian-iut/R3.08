from personnage import Personnage


class Guerrier(Personnage):
    def __init__(self, pseudo, niveau):
        """
            Méthode qui initialise une instance Guerrier et Personnage
        :param pseudo: Pseudo du Personnage
        :param niveau: Niveau du Personnage
        """
        self.__p = pseudo
        self.__n = niveau
        self.__v = niveau * 8 + 4
        self.__i = niveau * 4 + 6
        super().__init__(self.__p, self.__n)
        super().v(self.__v)
        super().i(self.__i)
