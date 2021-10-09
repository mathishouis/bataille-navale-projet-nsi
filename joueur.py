from case import Case

class Joueur(object):

    def __init__(self, pseudonyme: str):
        self.__pseudonyme = pseudonyme
        self.__cases_jouees = []

    def ajouter_case_jouee(self, case: Case):
        self.__cases_jouees.append(case)

    def retirer_case_jouee(self, case: Case):
        self.__cases_jouees.remove(case)

    def obtenir_cases_jouees(self) -> list:
        return self.__cases_jouees

    def placer_bateau(self, case: Case):
        self.__bateau = case

    def obtenir_case_bateau(self) -> Case:
        return self.__bateau

    def obtenir_pseudonyme(self) -> str:
        return self.__pseudonyme

    def vider_cases_jouees(self):
        self.__cases_jouees = []
