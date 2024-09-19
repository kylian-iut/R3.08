class Personnage:
    def __init__(self, pseudo : str, niveau : int = 1):
        """
            Méthode qui initialise le Personnage
        :param psoeudo: Nom donné au joueur
        :param niveau: Niveau d'avancement dans le jeu
        :param vie: Quantité de vie avant l'élimination
        :param initiative: C'est l'initiative
        """
        self.__p = pseudo
        self.__n = niveau
        self.__v = niveau
        self.__i = niveau

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, val):
        if isinstance(val, str):
            self.__p = val
        else:
            raise ValueError("p n'est pas une chaine")

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, val):
        if isinstance(val, int):
            if val >= 0:
                self.__n = val
            else:
                self.__n = 0
        else:
            raise ValueError("n n'est pas un entier")

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, val):
        if isinstance(val, int):
            if val >= 0:
                self.__v = val
            else:
                self.__v = 0
        else:
            raise ValueError("v n'est pas un entier")

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, val):
        if isinstance(val, int):
            if val >= 0:
                self.__i = val
            else:
                self.__i = 0
        else:
            raise ValueError("i n'est pas un entier")

    def attaque(self, camarade):
        if self.__i == camarade.__i:
            self.__v -= camarade.degats()
            camarade.__v -= self.degats()
        elif self.__i < camarade.__i:
            self.__v -= camarade.degats()
            if self.__v > 0:
                camarade.__v -= self.degats()
        else:
            camarade.__v -= self.degats()
            if camarade.__v > 0:
                self.__v -= camarade.degats()
    def combat(self, camarade):
        while self.__v > 0 and camarade.__v > 0:
            self.attaque(camarade)

    def soigner(self) -> int:
        if self.__v < self.__n:
            self.__v = self.__n
        return self.__v

    def degats(self) -> int:
        return self.__n




