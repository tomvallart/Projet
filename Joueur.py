# FILE: Joueur.py

class Joueur:
    def __init__(self, nom : str, jetons : int):
        str : self.nom = nom
        int : self.jetons = jetons
        list : self.cartes = []
        bool : self.couche = False

    def recevoir_carte(self, carte):
        self.cartes.append(carte)

    def miser(self, montant : int) -> int:
        if montant > self.jetons:
            raise ValueError("Montant de la mise supérieur aux jetons disponibles")
        self.jetons -= montant
        return montant

    def se_coucher(self):
        self.cartes = []
        self.couche = True
    
    def is_couche(self) -> bool:
        return self.couche
    
    def get_nom(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return f"Joueur {self.nom} avec {self.jetons} jetons et cartes: {self.cartes}"