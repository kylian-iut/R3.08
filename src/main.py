from guerrier import Guerrier
from mage import Mage
from joueur import Joueur
from personnage import Personnage


Me = Joueur("Kylian",5)
Gobi = Personnage("Gobi",2)
ng = Me.nperso(Gobi)
print(f"Nouveau personnage pour {Me.n} numéro : {ng}")
You = Joueur("Marc", 5)
Adela = Personnage("Adela",5)
na = You.nperso(Adela)
print(f"Nouveau personnage pour {You.n} numéro : {na}")
Gobi.attaque(Adela)
print(Gobi.v)
print(Adela.v)
print(Me.perso_pse("Gobi"))
Me.sperso_pse("Gobi")
print(Me.perso(Gobi))
