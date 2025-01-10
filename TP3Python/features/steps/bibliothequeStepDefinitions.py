from behave import *

from src.Bibliotheque import Bibliotheque


@given("Une bibliothèque vide")
def step_impl_given_vide(context):
    context.bibliotheque = Bibliotheque()


@given("Une bibliothèque avec {titre} par {auteur}")
def step_impl_given_avec(context, titre, auteur):
    context.bibliotheque = Bibliotheque()
    context.bibliotheque.ajouter_livre(titre, auteur)


@when("Un utilisateur ajoute le livre {titre} par {auteur}")
def step_impl_when_ajout(context, titre, auteur):
    context.resultat = context.bibliotheque.ajouter_livre(titre, auteur)


@then("La bibliothèque doit contenir {titre} par {auteur}")
def step_impl_then_ajout(context, titre, auteur):
    livres = context.bibliotheque.lister_livres()
    assert f"{titre} par {auteur}" in livres


@when("Un utilisateur recherche {mot_cle}")
def step_impl_when_recherche(context, mot_cle):
    context.resultat = context.bibliotheque.rechercher_livre(mot_cle)


@then("La recherche doit retourner {titre} par {auteur}")
def step_impl_then_recherche(context, titre, auteur):
    assert context.resultat == [{"titre": titre, "auteur": auteur}]


@when("Un utilisateur supprime le livre {titre}")
def step_impl_when_suppr(context, titre):
    context.resultat = context.bibliotheque.supprimer_livre(titre)


@then("La bibliothèque ne doit plus contenir {titre}")
def step_impl_then_suppr(context, titre):
    livres = context.bibliotheque.lister_livres()
    assert titre not in [livre.split(" par ")[0] for livre in livres]
