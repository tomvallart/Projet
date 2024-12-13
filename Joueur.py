# FILE: Joueur.py

class Joueur:
    def __init__(self, nom : str, jetons : int):
        self.nom = nom
        self.jetons = jetons
        self.cartes = []
        self.couche = False

    def recevoir_carte(self, carte):
        self.cartes.append(carte)
    
    def reset_cartes(self):
        self.cartes.clear()

    def miser(self, montant : int) -> int:
        if montant > self.jetons:
            raise ValueError("Montant de la mise supérieur aux jetons disponibles")
        self.jetons -= montant
        return montant

    def se_coucher(self):
        self.cartes = []
        self.couche = True
    
    def est_couche(self) -> bool:
        return self.couche
    
    def get_nom(self) -> str:
        return self.nom
    
    def get_jetons(self) -> str:
        return self.jetons

    def __repr__(self) -> str:
        return f"Joueur {self.nom} avec {self.jetons} jetons et cartes: {self.cartes}"