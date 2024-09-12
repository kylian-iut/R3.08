class Tasse:
    """
        Class qui caractérise un récient
    """
    matiere : str = "céramique"
    def __init__(self, couleur : str, contenance : int, marque : str, matiere = "céramique"):
        """
            méthode qui initialise la class Tasse. Unités: contenance est en ml
        """
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque
        self.matiere = matiere
    def __str__(self):
        return f"la tasse de matière {self.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml"
    def contenu(self, contenu : str):
        """
            méthode qui permet de définir le contenu comme un nouvel attribut d'instance
        """
        self.contenu = contenu
    def vide(self):
        """
            méthode qui permet de retirer l'attribut contenu de l'instance
        """
        del self.contenu

co = Tasse("blanc", 150, "Ikea")
co.contenu("café")
print(co)
print(f"contien du {co.contenu}")
print("il boit...")
co.vide()
print(co.contenu)
        

    
