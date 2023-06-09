from Zajecia_3.DeanerySystem.Day import Day


class Term(object):
    dniTygodnia = {Day.MON: "Poniedziałek", Day.TUE: "Wtorek", Day.WED: "Środa", Day.THU: "Czwartek",
                   Day.FRI: "Piątek", Day.SAT: "Sobota", Day.SUN: "Niedziela"}

    def __init__(self, day, hour, minute):
        self._day = day
        self.hour = hour
        self.minute = minute
        self.duration = 90

    def __str__(self):
        return self.dniTygodnia[self._day] + " " + str(self.hour) + ":" + str(self.minute) + " [" + str(self.duration) + "]"

    def earlierThan(self, termin):
        if self.hour < termin.__hour:
            return True
        if termin.__hour == self.hour and self.minute < termin.__minute:
            return True
        return False

    def laterThan(self, termin):
        return not self.earlierThan(termin)

    def equals(self, termin):
        if termin.__hour == self.hour and termin.__minute == self.minute:
            return True
        return False
