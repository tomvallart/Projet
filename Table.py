# FILE: Table.py

from Joueur import Joueur
from Carte import Carte
import random
from treys import Evaluator, Card

class Table:
    def __init__(self):
        self.joueurs = []
        self.cartes_communes = []
        self.paquet = self.creer_paquet()
        self.evaluator = Evaluator()

    def creer_paquet(self):
        valeurs = list(range(2, 15))  # 2 à 14 (As)
        couleurs = ['H', 'D', 'C', 'S']  # Coeur, Carreau, Trèfle, Pique
        paquet = []
        for couleur in couleurs:
            for valeur in valeurs:
                paquet.append(Carte(valeur, couleur))
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def distribuer_cartes(self):
        for joueur in self.joueurs:
            joueur.recevoir_carte(self.paquet.pop())
            joueur.recevoir_carte(self.paquet.pop())

    def distribuer_flop(self):
        for i in range(3):
            self.cartes_communes.append(self.paquet.pop())

    def distribuer_turn(self):
        self.cartes_communes.append(self.paquet.pop())

    def distribuer_river(self):
        self.cartes_communes.append(self.paquet.pop())

    def evaluer_meilleure_combinaison(self):
        meilleures_mains = {}
        cartes_communes_treys = []
        for carte in self.cartes_communes:
            cartes_communes_treys.append(Card.new(str(carte)))
        for joueur in self.joueurs:
            main_treys = []
            for carte in joueur.cartes:
                main_treys.append(Card.new(str(carte)))
            score = self.evaluator.evaluate(cartes_communes_treys, main_treys)
            meilleures_mains[joueur] = score
        gagnant = min(meilleures_mains, key=meilleures_mains.get)
        return gagnant

    def __repr__(self):
        return f"Table avec joueurs: {self.joueurs} et cartes communes: {self.cartes_communes}"

a = Table.creer_paquet()
print(a)