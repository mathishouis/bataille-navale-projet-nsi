from tkinter import *

from case import Case
from case import Etat
import random

class Grille(object):

    def __init__(self, f: Tk, largeur: int, hauteur: int):
        self.__f = f
        self.__largeur = largeur
        self.__hauteur = hauteur

        self.__creer_grille()

    def __creer_grille(self):
        print("Création d'une grille de taille " + str(self.__largeur) + "x" + str(self.__hauteur))

        self.__grille = []

        for x in range(self.__largeur):
            self.__grille.append([])
            for y in range(self.__hauteur):
                self.__grille[x].append([])
                self.__grille[x][y] = Case(self.__f, x, y)

    def vider_grille(self):
        for x in range(self.__largeur):
            for y in range(self.__hauteur):
                self.__grille[x][y].changer_etat(Etat.DISPONIBLE)

    def obtenir_grille(self) -> list:
        return self.__grille

    def obtenir_case(self, x, y) -> Case:
        return self.__grille[x][y]

    def obtenir_case_aleatoire(self) -> Case:
        return self.__grille[random.randint(0, self.__largeur) - 1][random.randint(0, self.__hauteur) - 1]

    def supprimer_grille(self):
        for x in range(self.__largeur):
            for y in range(self.__hauteur):
                self.__grille[x][y].obtenir_case().destroy()


