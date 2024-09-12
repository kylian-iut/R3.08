def affiche(texte : str):
    print(f"texte à afficher :  {texte}")

class Velo:
    """
        Class qui caractérise un vélo
    """
    def __init__(self, marque = "Yamaha", taille_pneu = 12, couleur = "gris", nb_vitesse = 6):
        """
            Méthode qui initialise une instance de vélo. Unités : taille_pneu en pouces
        """
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nb_vitesse = nb_vitesse
        self.vitesse = 3
    def gear_up(self):
        """
            Méthode qui augmmente la vitesse du vélo de 1 (max : nb_vitesse) et revoie la valeur actuelle
        """
        if self.vitesse < self.nb_vitesse:
            self.vitesse+=1
        print(self.vitesse)
    def gear_down(self):
        """
            Méthode qui baisse la vitesse du vélo de 1 (min : 1) et revoie la valeur actuelle
        """
        if self.nb_vitesse != 1:
            self.vitesse-=1
        print(self.vitesse)

def principale(str1):
    """
        Fonction qui simule l'utilisation du vélo
    """
    affiche(str1)
    v1 = Velo()
    v1.gear_up()
    v1.gear_up()
    v1.gear_down()
    v1.gear_up()
    v1.gear_up()
    v1.gear_down()

principale("Je fait du vélo")
    