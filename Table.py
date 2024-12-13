# FILE: Table.py

from Joueur import Joueur
from Carte import Carte
import random
from treys import Evaluator, Card

class Table:
    def __init__(self):
        self.joueurs = []
        self.cartes_communes = []
        self.paquet = []
        self.evaluator = Evaluator()

    def get_joueurs(self) :
        return self.joueurs
    
    def reset_paquet(self):
        self.paquet = []
        self.cartes_communes = []
    
    def creer_paquet(self):
        valeurs = list(range(2, 15))
        couleurs = ['H', 'D', 'C', 'S']  # Coeur, Carreau, Trèfle, Pique
        paquet = []
        for couleur in couleurs:
            for valeur in valeurs:
                paquet.append(Carte(valeur, couleur))
        self.paquet = paquet
    
    def melanger_paquet(self):
        random.shuffle(self.paquet)
        
    def montrer_paquet(self):
        print(self.paquet)

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
    
    def joueurs_actifs(self):
        joueurs_actifs = []
        for joueur in self.joueurs:
            if joueur.get_jetons() > 0:
                joueurs_actifs.append(joueur)
        return joueurs_actifs
    
    def evaluer_meilleure_combinaison(self):
        meilleures_mains = {}
        cartes_communes_treys = []
        for carte in self.cartes_communes:
            cartes_communes_treys.append(carte.treys_card)
        for joueur in self.joueurs:
            main_treys = []
            for carte in joueur.cartes:
                main_treys.append(carte.get_treys_card())
            score = self.evaluator.evaluate(cartes_communes_treys, main_treys)
            meilleures_mains[joueur] = score
        gagnant = min(meilleures_mains, key=meilleures_mains.get)
        return gagnant

    def print_table(self):
        joueurs = '\n'.join(map(str, self.joueurs)) if self.joueurs else "Aucun joueur"
        cartes = '\n'.join(map(str, self.cartes_communes)) if self.cartes_communes else "Aucune carte"
        print(f"Il y a {len(self.joueurs)} joueurs à la table")
        for joueur in self.joueurs:
            print(f"\nJoueur {joueur.get_nom()} a les cartes : ")
            for carte in joueur.get_cartes():
                carte.affiche_treys_card()
        print(f"\nLes cartes communes sont : ")
        for carte in self.cartes_communes:
            carte.affiche_treys_card()
        # return f"Table avec joueurs: {self.joueurs} et cartes communes: {self.cartes_communes}"

# t = Table()

# a = t.creer_paquet()
# print(a)

# t.melanger_paquet()
# t.montrer_paquet()
