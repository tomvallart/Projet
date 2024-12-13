class Joueur:
    """
    Classe représentant un joueur dans un jeu de cartes avec un système de mise.
    Attributs :
        nom (str) : Le nom du joueur.
        jetons (int) : Le nombre de jetons disponibles pour le joueur.
        cartes (list) : Les cartes détenues par le joueur.
        couche (bool) : Indique si le joueur s'est couché (abandon de la manche).
    """

    def __init__(self, nom: str, jetons: int):
        """
        Initialise un joueur avec un nom, un nombre de jetons et aucun carte au départ.
        Args:
            nom (str): Le nom du joueur.
            jetons (int): Le nombre initial de jetons du joueur.
        """
        self.nom = nom
        self.jetons = jetons
        self.cartes = []
        self.couche = False

    def recevoir_carte(self, carte):
        """
        Ajoute une carte à la main du joueur.
        Args:
            carte: La carte à ajouter à la main du joueur.
        """
        self.cartes.append(carte)

    def reset_cartes(self):
        """
        Réinitialise les cartes du joueur en vidant sa main.
        """
        self.cartes.clear()

    def miser(self, montant: int) -> int:
        """
        Permet au joueur de miser un montant spécifique de jetons.

        Args:
            montant (int): Le montant à miser.

        Returns:
            int: Le montant effectivement misé.

        Raises:
            ValueError: Si le montant de la mise dépasse les jetons disponibles.
        """
        if montant > self.jetons:
            raise ValueError("Montant de la mise supérieur aux jetons disponibles")
        self.jetons -= montant
        return montant

    def se_coucher(self):
        """
        Met le joueur en position couchée, indiquant qu'il abandonne la manche en cours.
        """
        self.cartes = []
        self.couche = True

    def est_couche(self) -> bool:
        """
        Vérifie si le joueur est couché.
        Returns:
            bool: True si le joueur est couché, sinon False.
        """
        return self.couche

    def get_nom(self) -> str:
        """
        Obtient le nom du joueur.
        Returns:
            str: Le nom du joueur.
        """
        return self.nom

    def get_jetons(self) -> int:
        """
        Obtient le nombre de jetons du joueur.
        Returns:
            int: Le nombre de jetons.
        """
        return self.jetons

    def recevoir_jetons(self, montant: int):
        """
        Ajoute un montant spécifique de jetons au joueur.
        Args:
            montant (int): Le nombre de jetons à ajouter.
        """
        self.jetons += montant

    def __repr__(self) -> str:
        """
        Représentation en chaîne de caractères de l'objet Joueur.
        Returns:
            str: Une chaîne représentant le joueur, ses jetons et ses cartes.
        """
        return f"Joueur {self.nom} avec {self.jetons} jetons et cartes: {self.cartes}"