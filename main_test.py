from Joueur import Joueur
from Carte import Carte
from Table import Table

def main():
    """ Moteur de jeu """

    # Initialisation du jeu
    print(" -------------------------------------------------------------")
    print(" ------------------------ Texas Hold'em ----------------------")
    print(" -------------------------------------------------------------")
    print(" --------- Tom LECLERCQ - Laurane MOURONVAL - Tom VALLART ----")
    print(" -------------------------------------------------------------")

    table = Table()
    creation_partie = False

    # Création des joueurs
    while not creation_partie :
        joueur = input("Indiquez le prénom du joueur à ajouter (Écrivez 'stop' pour arrêter) : ")
        if joueur.lower() == "stop":
            if len(table.get_joueurs()) >= 2 :
                creation_partie = True
                print("La partie peut commencer ! ")
            else :
                print("Il faut au moins deux joueurs pour démarrer la partie.")
        else :
            table.ajouter_joueur(Joueur(joueur, 100))
        

    partie_finie = False

    while not partie_finie:
        # Vérifier les joueurs actifs
        joueurs_actifs = table.joueurs_actifs()

        if len(joueurs_actifs) == 1:
            print(f"{joueurs_actifs[0].get_nom()} a gagné la partie!")
            partie_finie = True
            break

        # Préparer la manche
        table.creer_paquet()
        table.melanger_paquet()
        table.distribuer_cartes()
        table.distribuer_flop()

        manche_finie = False
        cagnotte = 0
        nb_joueurs_couches = 0
        index = 0

        while not manche_finie:
            print("-----------------------------------------------------------")
            print(table)
            joueurs_actifs = table.joueurs_actifs()
            if len(joueurs_actifs) == 1:
                print(f"{joueurs_actifs[0].get_nom()} remporte la manche et gagne {cagnotte} jetons !")
                joueurs_actifs[0].recevoir_jetons(cagnotte)
                manche_finie = True
                break

            joueur_actuel = joueurs_actifs[index % len(joueurs_actifs)]

            if joueur_actuel.est_couche():
                print(f"Le joueur {joueur_actuel.get_nom()} est couché et passe son tour.")
                index += 1

            print(f"\nC'est au tour de {joueur_actuel.get_nom()}.")
            print("Actions possibles : \n1. Miser \n2. Se coucher")

            choix = int(input("Votre choix : "))

            if choix == 1:
                montant = int(input("Montant de la mise : "))
                joueur_actuel.miser(montant)
                cagnotte += montant
                print(f"{joueur_actuel.get_nom()} mise {montant} jetons. La cagnotte est maintenant de {cagnotte}.")
                index += 1
            elif choix == 2:
                joueur_actuel.se_coucher()
                print(f"{joueur_actuel.get_nom()} s'est couché.")
                nb_joueurs_couches += 1
                index += 1
            else:
                print("auvaise nouvelle, il faut mieux jouer :) Veuillez choisir 1 ou 2.")

            # Gestion des étape de distribution de cartes
            if index == len(joueurs_actifs):
                table.distribuer_turn()
                print("\n\nTurn distribué.")
            elif index == len(joueurs_actifs) * 2:
                table.distribuer_river()
                print("\n\nRiver distribué.")
            elif index >= len(joueurs_actifs) * 3:
                gagnant = table.evaluer_meilleure_combinaison()
                print(f"\n\nLe gagnant de la manche est {gagnant.get_nom()} qui remporte {cagnotte} jetons.")
                gagnant.recevoir_jetons(cagnotte)
                manche_finie = True

        # Réinitialiser les mains de chaque joueur actif
        for joueur in table.get_joueurs():
            joueur.reset_cartes()

if __name__ == '__main__':
    main()
