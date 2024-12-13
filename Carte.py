# FILE: Carte.py

from treys import Card

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.treys_card = Card.new(f"{self.get_valeur_str()}{self.get_couleur_str()}")
        
    def get_treys_card(self):
        return self.treys_card
    
    def affiche_treys_card(self):
        Card.print_pretty_card(self.treys_card)
    
    def get_valeur(self) -> int:
        return self.valeur

    def set_valeur(self, valeur):
        self.valeur = valeur
        self.treys_card = Card.new(f"{self.get_valeur_str()}{self.get_couleur_str()}")

    def get_couleur(self) -> str:
        return self.couleur

    def set_couleur(self, couleur):
        self.couleur = couleur
        self.treys_card = Card.new(f"{self.get_valeur_str()}{self.get_couleur_str()}")

    def get_valeur_str(self) -> str:
        valeurs = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        return valeurs[self.valeur]

    def get_couleur_str(self) -> str:
        couleurs = {'H': 'h', 'D': 'd', 'C': 'c', 'S': 's'}
        return couleurs[self.couleur]

    def __repr__(self):
        valeurs = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
        couleurs = {'H': 'Coeur', 'D': 'Carreau', 'C': 'Trèfle', 'S': 'Pique'}
        valeur_str = valeurs[self.valeur]
        couleur_str = couleurs[self.couleur]
        return f"{valeur_str} de {couleur_str}"