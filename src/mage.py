from personnage import Personnage

class Mage(Personnage):
    def __init__(self, pseudo, niveau):
        """
            Méthode qui initialise une instance Guerrier et Personnage
        :param pseudo: Pseudo du Personnage
        :param niveau: Niveau du Personnage
        """
        self.__p = pseudo
        self.__n = niveau
        self.__v = niveau*5+10
        self.__i = niveau*6+4
        self.__m = niveau*5
        super().__init__(self.__p, self.__n)
        super().v(self.__v)
        super().i(self.__i)
