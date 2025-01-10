class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur):
        self.livres.append({"titre": titre, "auteur": auteur})
        return f"Livre '{titre}' par {auteur} ajouté."

    def rechercher_livre(self, mot_cle):
        resultats = [
            livre
            for livre in self.livres
            if mot_cle.lower() in livre["titre"].lower()
            or mot_cle.lower() in livre["auteur"].lower()
        ]
        if resultats:
            return resultats
        return "Aucun livre trouvé."

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre["titre"].lower() == titre.lower():
                self.livres.remove(livre)
                return f"Livre '{titre}' supprimé."
        return "Livre non trouvé."

    def lister_livres(self):
        if not self.livres:
            return "Aucun livre dans la bibliothèque."
        return [f"{livre['titre']} par {livre['auteur']}" for livre in self.livres]


# Exemple d'utilisation
if __name__ == "__main__":
    biblio = Bibliotheque()

    # Ajout de livres
    print(biblio.ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry"))
    print(biblio.ajouter_livre("1984", "George Orwell"))

    # Liste des livres
    print("Livres disponibles :", biblio.lister_livres())

    # Recherche de livre
    print("Recherche 'Orwell' :", biblio.rechercher_livre("Orwell"))

    # Suppression d'un livre
    print(biblio.supprimer_livre("1984"))
    print("Livres disponibles :", biblio.lister_livres())
