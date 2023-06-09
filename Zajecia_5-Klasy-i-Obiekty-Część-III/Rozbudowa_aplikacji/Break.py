from Zajecia_4.DeanerySystem.Term import Term
from Zajecia_5.Mechanizm_dziedziczenia.BasicTerm import BasicTerm


class Break:
    def __init__(self, term: BasicTerm):
        self.term = term

    def __str__(self):
        return "---"

    def getTerm(self):
        return str(self.term.hour) + ":" + str(self.term.minute) + " [" + str(
            self.term.duration) + ']'
