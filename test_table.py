# FILE: test_table.py

from Table import Table
from Joueur import Joueur
from Carte import Carte

def test_evaluer_meilleure_combinaison():
    # Créer une table
    table = Table()

    # Ajouter des joueurs
    joueur1 = Joueur("Alice", 100)
    joueur2 = Joueur("Bob", 100)
    table.ajouter_joueur(joueur1)
    table.ajouter_joueur(joueur2)

    # Distribuer des cartes aux joueurs
    joueur1.recevoir_carte(Carte(14, 'H'))  # As de Coeur
    joueur1.recevoir_carte(Carte(13, 'H'))  # Roi de Coeur
    joueur2.recevoir_carte(Carte(12, 'S'))  # Dame de Pique
    joueur2.recevoir_carte(Carte(11, 'S'))  # Valet de Pique

    # Distribuer les cartes communes
    table.cartes_communes = [
        Carte(10, 'S'),  # 10 de Coeur
        Carte(9, 'S'),   # 9 de Coeur
        Carte(8, 'S'),   # 8 de Coeur
        Carte(7, 'D'),   # 7 de Carreau
        Carte(6, 'C')    # 6 de Trèfle
    ]
    cartes_str = ' '
    for carte in table.cartes_communes:
        # carte.affiche_treys_card()
        cartes_str.join([carte.pretty_print() for carte in self.cartes])

    print(cartes_str)
    # Évaluer la meilleure combinaison
    gagnant = table.evaluer_meilleure_combinaison()

    # Afficher le gagnant
    print(f"Le gagnant est {gagnant.nom} avec la meilleure combinaison.")

if __name__ == "__main__":
    test_evaluer_meilleure_combinaison()