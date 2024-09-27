from personnage import Personnage

class Joueur:
    def __init__(self, nom : str, n_max_person : int):
        """
            Méthode qui initialise une instance de Joueur
        :param nom:  Nom du joueur
        :param n_max_person: Quantité maximal de personnage
        """
        self.__n = nom
        self.__m = n_max_person
        self.__e = []

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, val):
        if isinstance(val, str):
            self.__n = val
        else:
            raise ValueError("n n'est pas une chaine")

    @property
    def m(self):
        return self.__m
    @m.setter
    def m(self, val):
        if isinstance(val, int):
            if val >= 1:
                self.__m = val
            else:
                self.__m = 1
        else:
            raise ValueError("m n'est pas un entier")

    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, val):
        if isinstance(val, list):
            self.__e = val
        else:
            raise ValueError("e n'est pas une liste")

    def nperso(self, perso : Personnage) -> int:
        """
            Méthode qui permet d'ajouter un personnage à un jouer
        :param perso: Objet personnage
        :return: Numéro du personnage chez le joueur
        """
        self.e.append(perso)
        if len(self.e) > self.__m:
            self.e.pop(self.__m)
            return f"Maximum de personnage atteint : {self.__m}"
        else:
            return len(self.e)

    def perso_num(self,numero : int):
        """
            Méthode qui donne l'objet Personnage selon son numéro
        :param numero: Numéro du Personnage chez le joueur
        """
        try:
            return self.e[numero]
        except all as err:
            exit(err)

    def perso_pse(self,pseudo:str):
        """
            Méthode qui donne l'objet Personnage selon son pseudo
        :param pseudo: Pseudo du Personnage
        :return: Personnage
        """
        for perso in self.e:
            if perso.p == pseudo:
                return perso

    def perso(self, perso:Personnage):
        """
            Méthode qui donne le personnage selon un objet Personnage
        :param perso: Personnage
        :return: Personnage
        """
        for ele in self.e:
            if perso.__eq__ == ele.__eq__:
                return ele
    def sperso_num(self, numero : int):
        """
            Méthode qui supprime un Personnage selon son numéro chez le joueur
        :param numero: Numéro du Personnage chez le joueur
        """
        try:
            self.e.pop(numero)
        except all as err:
            exit(err)

    def sperso_pse(self, pseudo:str):
        """
            Méthode qui supprime un Personnage selon son pseudo
        :param pseudo: Pseudo du Personnage
        """
        i=0
        for perso in self.e:
            if perso.p == pseudo:
                self.e.pop(i)
            i+=1
    def sperso(self, perso : Personnage):
        """
            Méthode qui supprime un Personnage selon un objet Personnage
        :param perso: Personnage
        """
        i=0
        for ele in self.e:
            if perso.__eq__ == ele.__eq__:
                self.e.pop(i)
            i+=1

kyks = Joueur("Kylian",1)
bob = Personnage("Bob")
bobette = Personnage("Bobette")
print(kyks.nperso(bob))
print(kyks.nperso(bobette))


