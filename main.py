import time
from tkinter import *

from joueur import Joueur
from case import Etat
from fenetre import *
import random

class BatailleNavale(object):

    def __init__(self):
        self.__f = Tk()
        self.__f.title("Bataille Navale 5x5")
        self.__f.resizable(False, False)

        self.__joueurs = self.__demander_joueurs()
        self.__lancer_partie()

    def __demander_joueurs(self) -> Joueur:
        fenetre_pseudo = DemandeJoueur(self.__f)
        for i in range(9):
            fenetre_pseudo.changer_titre_fenetre(" Entrez le pseudonyme du joueur " + str(i) + ": ")
            fenetre_pseudo.obtenir_bouton_valider().wait_variable(fenetre_pseudo.obtenir_etat_bouton_valider())
        fenetre_pseudo.supprimer_fenetre()
        return fenetre_pseudo.obtenir_joueurs()

    def __placer_bateaux(self, joueurs: list):
        for joueur in joueurs:
            joueur.placer_bateau(self.__grille.obtenir_case_aleatoire())

    def __lancer_partie(self):
        fenetre_grille = AfficherGrille(self.__f, 5, 5, 3)
        self.__grille = fenetre_grille.obtenir_grille()

        joueurs_aleatoires = random.sample(self.__joueurs, 2)
        fenetre_grille.changer_message_info(joueurs_aleatoires[0].obtenir_pseudonyme() + " joue contre " + joueurs_aleatoires[1].obtenir_pseudonyme())
        fenetre_grille.changer_texte_bouton_valider("Commencer")
        fenetre_grille.obtenir_bouton_valider().pack()
        fenetre_grille.changer_selection(3)
        fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())
        fenetre_grille.changer_selection(0)
        self.__placer_bateaux(joueurs_aleatoires)
        tour = 0
        jouer = True

        while jouer:
            if (tour % 2) == 0:
                joueur = joueurs_aleatoires[0]
                fenetre_grille.changer_message_info("Au tour de " + joueurs_aleatoires[0].obtenir_pseudonyme())
            else:
                joueur = joueurs_aleatoires[1]
                fenetre_grille.changer_message_info("Au tour de " + joueurs_aleatoires[1].obtenir_pseudonyme())
            fenetre_grille.changer_texte_bouton_valider("Valider")
            fenetre_grille.vider_grille()
            fenetre_grille.obtenir_bouton_valider().pack_forget()

            for case in joueur.obtenir_cases_jouees():
                fenetre_grille.obtenir_grille().obtenir_case(case.obtenir_x(), case.obtenir_y()).changer_etat(Etat.INDISPONIBLE)

            fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())

            for case in fenetre_grille.obtenir_cases_selectionnees():
                fenetre_grille.obtenir_grille().obtenir_case(case.obtenir_x(), case.obtenir_y()).changer_etat(Etat.INDISPONIBLE)
                joueur.ajouter_case_jouee(case)
                if joueur.obtenir_case_bateau() == case:
                    fenetre_grille.changer_message_info("Victoire de " + joueur.obtenir_pseudonyme())
                    case.changer_etat(Etat.DECOUVERTE)
                    fenetre_grille.changer_texte_bouton_valider("Continuer le tournoi")
                    fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())
                    joueur.vider_cases_jouees()
                    if (tour % 2) == 0:
                        self.__joueurs.remove(joueurs_aleatoires[1])
                    else:
                        self.__joueurs.remove(joueurs_aleatoires[0])
                    jouer = False
                    break


            tour += 1
        if len(self.__joueurs) == 1:
            fenetre_grille.changer_message_info(self.__joueurs[0].obtenir_pseudonyme() + " remporte le tournoi!")
            fenetre_grille.changer_texte_bouton_valider("Recommencer")
            fenetre_grille.obtenir_bouton_valider().wait_variable(fenetre_grille.obtenir_etat_bouton_valider())
            fenetre_grille.supprimer_fenetre()
            self.__joueurs = self.__demander_joueurs()
            self.__lancer_partie()
        else:
            fenetre_grille.supprimer_fenetre()
            self.__lancer_partie()

    def demarrer(self):
        self.__f.mainloop()

main = BatailleNavale()
main.demarrer()