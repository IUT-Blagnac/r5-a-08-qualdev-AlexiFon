Feature: Gestion des Livres dans une Bibliothèque
    Gestion simple des livres avec recherche, ajout et suppression.

Scenario Outline: Ajouter un livre dans la bibliothèque
    Given Une bibliothèque vide
    When Un utilisateur ajoute le livre <titre> par <auteur>
    Then La bibliothèque doit contenir <titre> par <auteur>

    Examples: Ajouter un livre dans la bibliothèque
        | titre | auteur |
        | 1984  | George Orwell |
        | Le Seigneur des Anneaux | J.R.R. Tolkien |

Scenario Outline: Rechercher un livre dans la bibliothèque
    Given Une bibliothèque avec <titre> par <auteur>
    When Un utilisateur recherche <mot-cle>
    Then La recherche doit retourner <titre> par <auteur>

    Examples: Rechercher un livre dans la bibliothèque
        | titre | auteur | mot-cle |
        | 1984  | George Orwell | 1984 |
        | Le Seigneur des Anneaux | J.R.R. Tolkien | Anneaux |

Scenario Outline: Supprimer un livre de la bibliothèque
    Given Une bibliothèque avec <titre> par <auteur>
    When Un utilisateur supprime le livre <titre>
    Then La bibliothèque ne doit plus contenir <titre>

    Examples: Supprimer un livre de la bibliothèque
        | titre | auteur         |
        | 1984  | George Orwell  |
        | Le Seigneur des Anneaux | J.R.R. Tolkien |
