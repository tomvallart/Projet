import Joueur
import Carte
import Table


def main():
    """ moteur de jeu """
    j1 = Joueur("Brandon", 100)
    j2 = Joueur("John", 100)

    table = Table()
    table.ajouter_joueur(j1)
    table.ajouter_joueur(j2)
    table.distribuer_cartes()



    # j1.recevoir_carte(Carte())




   

if __name__ == '__main__':
    main() 