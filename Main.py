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

    creation_partie = False
    table = Table()
    
    while not creation_partie:
        joueur = input("Indiquez le prénom du joueur à ajouter (Écrivez 'stop' pour arrêter) : ")
        if joueur == "stop" :
            creation_partie = True
        else:
            table.ajouter_joueur(Joueur(joueur, 100))
    
    partie_finie = False
    manche_finie = False
    index = 0
    cagnotte = 0
    nb_jr_couches = 0

    while not partie_finie :
        j_actifs = table.joueurs_actifs()
        nb_joueurs = len(j_actifs)

        if len(j_actifs) > 1:
            manche_finie = False
        else:
            print(f"{j_actifs[0].get_nom()} a gagné la partie")
            partie_finie = True
            manche_finie = True
            
        # etape = 0 : le flop = 3 premières cartes dévoilées
        # etape = 1 : le turn = 1 carte dévoilée
        # etape = 2 : le river = 1 carte dévoilée
            
        while not manche_finie :
            if index == 0 :
                table.creer_paquet()
                table.melanger_paquet()
                table.distribuer_cartes()
                table.distribuer_flop()
                
            elif index == len(j_actifs) :
                table.distribuer_turn()

            elif index == len(j_actifs) * 2 :
                table.distribuer_river()

            elif (index == len(j_actifs) * 3) or (nb_jr_couches == nb_joueurs-1):
                gagnant_manche = table.evaluer_meilleure_combinaison()
                print(f"Le gagnant de la manche est {gagnant_manche.get_nom()} et reçoit {cagnotte} jetons !")
                manche_finie = True
                index = 0
                cagnotte = 0
                nb_jr_couches = 0
                gagnant_manche.recevoir_jetons(cagnotte)
                break
            # 
            
            print(table)

            joueur_actuel = table.get_joueurs()[index%nb_joueurs]

            # si le joueur est couché = il passe son tour, sinon il joue
            if not joueur_actuel.est_couche():
                print(f"\nC'est au tour du joueur {joueur_actuel.get_nom()}")
                print("\nAction possibles : \n1. Miser \n2. Se coucher ")
                reponse = int(input('Votre choix : '))

                if reponse == 1:
                    montant = int(input('\nMontant de la mise : '))
                    joueur_actuel.miser(montant)
                    cagnotte += montant
                    print(f"Le joueur {joueur_actuel.get_nom()} mise {montant} jetons")
                    index += 1
                elif reponse == 2:
                    joueur_actuel.se_coucher()
                    nb_jr_couches += 1
                    index += 1
                else :
                    print("Mauvaise nouvelle, il faut mieux jouer :) Merci de choisir une action parmis la liste")
            else:
                print(f"Le joueur {joueur_actuel.get_nom()} est couché il passe son tour")
                index += 1
            
            print ("\n----------------------------------------------------------------------------\n")
        
        # fin de la manche : on enlève les cartes de la main des joueurs
        for joueur in table.get_joueurs():
            joueur.reset_cartes()

if __name__ == '__main__':
    main()