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



