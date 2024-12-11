# FILE: Carte.py

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def 

    # Équivalent au ToString
    def __repr__(self):
        valeurs = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
        couleurs = {'H': 'Coeur', 'D': 'Carreau', 'C': 'Trèfle', 'S': 'Pique'}
        valeur = valeurs[self.valeur]
        couleur = couleurs[self.couleur]
        return f"{valeur} de {couleur}"

carte = Carte(2,"H")
print(carte)