class MaClasse :
    monAttributClasse : str = "bonjour"
    def __init__ ( self , valeur : int ):
        self . monAttributInstance = valeur

mc = MaClasse (12)
print (f"{mc} , {mc. monAttributClasse } ,{ mc. monattributInstance }")

class Tasse:
    matiere : str = "céramique"
    def __init__(self, couleur : str, contenance : int, marque : int):
        """
            fonction qui initialise la class Tasse. Unités: contenance est en ml
        """
        self.color = couleur
        self.conte = contenance
        self.socie = marque
    def __str__(self):
        return f"la tasse de matière {self}, de couleur {self.color} et de marque {self.socie} a une
contenance de {self.conte} ml"
    
