from Joueur import Joueur
from Carte import Carte
from Table import Table


def main():
    """ Moteur de jeu """

    # Initialisation du jeu
    print(" -------------------------------------------------------------------")
    print(" -------------------------- Texas Hold em --------------------------")
    print(" -------------------------------------------------------------------")
    print(" --------- Tom LECLERCQ - Laurane MOURONVAL - Tom VALLART ----------")
    print(" -------------------------------------------------------------------")

    j1 = Joueur("Brandon", 100)
    j2 = Joueur("John", 100)
    nb_joueurs = 2

    table = Table()
    table.ajouter_joueur(j1)
    table.ajouter_joueur(j2)

    table.melanger_paquet()
    table.distribuer_cartes()

    table.distribuer_flop()
    print(table)

# while partie_finie = False

    manche_finie = False
    index = 0

    while not manche_finie :
        joueur_actuel = table.get_joueurs[index%nb_joueurs]

        # si le joueur est couché = il passe son tour sinon il joue
        if not joueur_actuel.est_couche():
            print("Action possibles : \n1. Miser \n2. Se coucher ")
            reponse = int(input('Votre choix : '))

            if reponse == 1:
                montant = int(input('Montant de la mise : '))
                joueur_actuel.miser(montant)
            elif reponse == 2:
                joueur_actuel.se_coucher()
            else :
                print("Mauvaise nouvelle, il fallait mieux jouer :)")
        else:
            print(f"Le joueur {joueur_actuel.get_nom()} est couché il passe son tour")
        

        # si joueur n'a plus de jeton = eliminé = fin de partie
        
        index += 1
        manche_finie = True

    


if __name__ == '__main__':
    main() 