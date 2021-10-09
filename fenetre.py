from tkinter import *

from joueur import Joueur
from grille import Grille
from case import Etat

class DemandeJoueur(object):

    def __init__(self, f: Tk):
        self.__f = f
        self.__joueurs = []

        self.__creer_fenetre()

    def __creer_fenetre(self):
        # Redimensionnement de la fenêtre
        self.__f.minsize(width=250, height=80)
        self.__f.maxsize(width=250, height=80)

        # Titre
        self.__titre_texte = StringVar()
        self.__titre = Label(self.__f, textvariable=self.__titre_texte, relief=RAISED)
        self.__titre.place(x=10, y=5, width=230, height=20)
        self.__titre_texte.set("Bataille Navale")

        # Saisie du pseudonyme
        self.__entree_pseudonyme = Entry(self.__f)
        self.__entree_pseudonyme.place(x=20, y=30, width=210, height=20)

        # Bouton valider
        self.__etat_bouton_valider = IntVar()
        self.__bouton_valider = Button(self.__f, text="Valider", command=lambda: self.__valider_pseudonyme(self.__entree_pseudonyme))
        self.__bouton_valider.place(x=20, y=50, width=210, height=20)

    def __valider_pseudonyme(self, entree: Entry):
        self.__etat_bouton_valider.set(1)
        self.__joueurs.append(Joueur(entree.get()))
        entree.delete(0, 'end')

    def changer_titre_fenetre(self, titre: str):
        self.__titre_texte.set(titre)

    def obtenir_bouton_valider(self) -> Button:
        return self.__bouton_valider

    def obtenir_etat_bouton_valider(self) -> IntVar:
        return self.__etat_bouton_valider

    def obtenir_joueurs(self) -> list:
        return self.__joueurs

    def supprimer_fenetre(self):
        self.__titre.destroy()
        self.__entree_pseudonyme.destroy()
        self.__bouton_valider.destroy()

class AfficherGrille(object):

    def __init__(self, f: Tk, largeur: int, hauteur: int, selection_max: int):
        self.__f = f
        self.__hauteur_grille = largeur
        self.__largeur_grille = hauteur
        self.__selection_max = selection_max
        self.__selection = 0

        self.__creer_fenetre()

    def __creer_fenetre(self):
        # Redimensionnement de la fenêtre
        self.__f.minsize(width=50 * self.__largeur_grille, height=50 * self.__hauteur_grille)
        self.__f.maxsize(width=50 * self.__largeur_grille, height=60 * self.__hauteur_grille)

        # Canvas
        self.__canvas = Canvas(self.__f, width=50 * self.__largeur_grille, height=50 * self.__hauteur_grille, bg='white')
        self.__canvas.pack()

        # Message d'info
        self.__info_texte = StringVar()
        self.__info = Label(self.__f, textvariable=self.__info_texte, relief=SUNKEN)
        self.__info.pack()
        self.__info_texte.set(" Au tour de Roger ")

        # Grille
        self.__grille = Grille(self.__f, self.__largeur_grille, self.__hauteur_grille)

        # Interaction fenêtre
        self.__f.bind("<1>", self.__cliquer_fenetre)

        # Bouton valider
        self.__etat_bouton_valider = IntVar()
        self.__bouton_valider_texte = StringVar()
        self.__bouton_valider = Button(self.__f, textvariable=self.__bouton_valider_texte, command=lambda: self.__valider_tour())

    def __cliquer_fenetre(self, event):
        for x in range(self.__largeur_grille):
            for y in range(self.__hauteur_grille):
                case = self.__grille.obtenir_case(x, y)
                if case.obtenir_case() == event.widget:
                    if case.obtenir_etat_case() == Etat.DISPONIBLE:
                        if self.__selection < self.__selection_max:
                            self.__selection += 1
                            case.changer_etat(Etat.SELECTIONNEE)
                    elif case.obtenir_etat_case() == Etat.SELECTIONNEE:
                        self.__selection -= 1
                        case.changer_etat(Etat.DISPONIBLE)
        if self.__selection == self.__selection_max:
            self.__bouton_valider.pack()
        else:
            self.__bouton_valider.pack_forget()

    def __valider_tour(self):
        self.__etat_bouton_valider.set(1)

    def obtenir_grille(self) -> Grille:
        return self.__grille

    def obtenir_bouton_valider(self) -> Button:
        return self.__bouton_valider

    def obtenir_etat_bouton_valider(self) -> IntVar:
        return self.__etat_bouton_valider

    def vider_grille(self):
        self.__grille.vider_grille()
        self.__selection = 0

    def obtenir_cases_selectionnees(self) -> list:
        cases = []
        for x in range(self.__largeur_grille):
            for y in range(self.__hauteur_grille):
                case = self.__grille.obtenir_case(x, y)
                if case.obtenir_etat_case() == Etat.SELECTIONNEE:
                    cases.append(case)
        return cases

    def changer_message_info(self, texte: str):
        self.__info_texte.set(texte)

    def changer_texte_bouton_valider(self, texte: str):
        self.__bouton_valider_texte.set(texte)

    def supprimer_fenetre(self):
        self.__canvas.destroy()
        self.__info.destroy()
        self.__grille.supprimer_grille()
        self.__bouton_valider.destroy()
        self.__f.unbind("<1>")

    def changer_selection(self, selection: int):
        self.__selection = selection




