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
        """
            Méthode qui permet l'attaque conventionnel entre deux Personnanges
        :param camarade: autre Personnage
        """
        if self.i == camarade.i:
            self.v -= camarade.degats()
            camarade.v -= self.degats()
        elif self.i < camarade.i:
            self.v -= camarade.degats()
            if self.v > 0:
                camarade.v -= self.degats()
        else:
            camarade.v -= self.degats()
            if camarade.v > 0:
                self.v -= camarade.degats()
    def combat(self, camarade):
        """
            Méthode qui utilise en boucle la méthode attaque jusqu'à que la vie d'un Personnage tombe à 0
        :param camarade: autre Personnage
        """
        while self.v > 0 and camarade.v > 0:
            self.attaque(camarade)

    def soigner(self) -> int:
        """
            Méthode qui permet de réstaurer la vie du Personnage
        :return: Nombre de point de vie
        """
        if self.v < self.n:
            self.v = self.n
        return self.v

    def degats(self) -> int:
        """
            Méthode qui fournit la quanbtité de dégat infligé par le Personnage
        :return: Quantité de dégats
        """
        return self.n






