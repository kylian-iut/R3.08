"""
    Exercice 1.2 - J'ai écrit les fonctions suivantes
"""

def addition (a : int , b : int ) -> int :
    """
        fonction d’addition de deux nombres entiers
    """
    return a + b

def maximum (a : int , b: int ) -> int :
    """
        fonction qui fourni le maximum entre deux nombre entiers
    """
    if a > b:
        return a
    else:
        return b
    
def seuil (x : int , s : int = 10) -> bool:
    """
        fonction qui vérifie si la valeur dépasse un seuil (10 par défaut)
    """
    if x > s:
        return True
    else:
        return False

def plusgrand (lst : int = []) -> int:
    """
        fonction qui fourni la valeur maximum de la liste
    """
    h=lst[0]
    for x in lst:
        if x > h:
            h = x
    return h

def smallist (lst : int = [], s : int = 3) -> bool:
    """
        fonction qui vérifie si la longeur de la liste dépasse un seuil (3 par défaut)
    """
    if len(lst) > s:
        return True
    else:
        return False

def repeat (pre : str,**dict : str) -> str:
    """
        fonction qui affiche une chaîne qui précédera l'ensemble des données d'un dictionnaire
    """
    txt=""
    for elm in dict:
        txt=txt+pre+" "+elm+"\n"
    return txt