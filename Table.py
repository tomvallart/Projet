# FILE: Table.py

from Carte import Carte
from Joueur import Joueur
import random


class Table:
    def __init__(self):
        self.joueurs = []
        self.cartes_communes = []
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = list(range(2, 15))  # 2 à 14 (As)
        couleurs = ['H', 'D', 'C', 'S']  # Coeur, Carreau, Trèfle, Pique
        return [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def distribuer_cartes(self):
        for joueur in self.joueurs:
            joueur.recevoir_carte(self.paquet.pop())
            joueur.recevoir_carte(self.paquet.pop())

    def distribuer_flop(self):
        self.cartes_communes.extend([self.paquet.pop() for _ in range(3)])

    def distribuer_turn(self):
        self.cartes_communes.append(self.paquet.pop())

    def distribuer_river(self):
        self.cartes_communes.append(self.paquet.pop())

    def __repr__(self):
        return f"Table avec joueurs: {self.joueurs} et cartes communes: {self.cartes_communes}"