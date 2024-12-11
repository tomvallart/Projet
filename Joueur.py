# FILE: Joueur.py

class Joueur:
    def __init__(self, nom, jetons):
        self.nom = nom
        self.jetons = jetons
        self.cartes = []

    def recevoir_carte(self, carte):
        self.cartes.append(carte)

        
    def recevoir_carte_rd(self, carte):
        # attribue une carte aléatoire
        self.cartes.append(carte)

    def miser(self, montant):
        if montant > self.jetons:
            raise ValueError("Montant de la mise supérieur aux jetons disponibles")
        self.jetons -= montant
        return montant

    def se_coucher(self):
        self.cartes = []

    def __repr__(self):
        return f"Joueur {self.nom} avec {self.jetons} jetons et cartes: {self.cartes}"