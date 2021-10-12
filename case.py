from tkinter import *

from enum import Enum

class Etat(Enum):
    DISPONIBLE = 0
    INDISPONIBLE = 1
    SELECTIONNEE = 2
    DECOUVERTE = 3

class Case(object):

    def __init__(self, f: Tk, x: int, y: int):
        self.__f = f
        self.__x = x
        self.__y = y
        self.__etat = Etat.DISPONIBLE

        self.__case = Button(f)
        self.__case.place(x=x * 50, y=y * 50, width=50, height=50)

    def changer_etat(self, etat: int):
        self.__etat = etat

        if self.__etat == Etat.DISPONIBLE:
            self.__case.configure(bg='#d9d9d9')
        elif self.__etat == Etat.SELECTIONNEE:
            self.__case.configure(bg='#ffffff')
        elif self.__etat == Etat.INDISPONIBLE:
            self.__case.configure(bg='#919191')
        else:
            self.__case.configure(bg='#008f0e')

    def obtenir_etat_case(self) -> int:
        return self.__etat

    def obtenir_case(self) -> Button:
        return self.__case

    def obtenir_x(self) -> int:
        return self.__x

    def obtenir_y(self) -> int:
        return self.__y
