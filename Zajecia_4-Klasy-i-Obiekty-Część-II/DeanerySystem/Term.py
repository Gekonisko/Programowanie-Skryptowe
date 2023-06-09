from Zajecia_4.DeanerySystem.Day import Day


class Term(object):
    dniTygodnia = {Day.MON: "Poniedziałek", Day.TUE: "Wtorek", Day.WED: "Środa", Day.THU: "Czwartek",
                   Day.FRI: "Piątek", Day.SAT: "Sobota", Day.SUN: "Niedziela"}

    def __init__(self, day, hour, minute, duration=90):
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration

    def earlier_time_Term(self):
        minutes = self.__minute - self.__duration
        hour = self.hour
        if minutes <= 0:
            hour -= 1
            minutes = 60 + minutes
        return Term(day=self.day, hour=hour, minute=minutes, duration=self.duration)

    def end_time(self):
        minutes = self.__minute + self.__duration
        hour = self.hour
        if minutes >= 60:
            hour += int(minutes / 60)
            minutes %= 60
        return f'{hour}:{minutes}'

    def end_time_Term(self):
        minutes = self.__minute + self.__duration
        hour = self.hour
        if minutes <= 0:
            hour += int(minutes / 60)
            minutes %= 60
        return Term(day=self.day, hour=hour, minute=minutes, duration=self.duration)

    @property
    def day(self):
        return self.__day

    @property
    def hour(self):
        return self.__hour

    @property
    def minute(self):
        return self.__minute

    @property
    def duration(self):
        return self.__duration

    @day.setter
    def day(self, var):
        self.__day = var

    @hour.setter
    def hour(self, var):
        self.__hour = var

    @minute.setter
    def minute(self, var):
        self.__minute = var

    @duration.setter
    def duration(self, var):
        self.__duration = var

    def isOverlappingLater(self, term):
        start = (self.hour * 60) + self.minute
        endTerm = self.end_time_Term()
        end = (endTerm.hour * 60) + endTerm.minute
        termStart = term.hour * 60 + term.minute
        termEndTerm = term.end_time_Term()
        termEnd = termEndTerm.hour * 60 + termEndTerm.minute
        if start < termStart < end or start < termEnd < end or (termStart < start and termEnd > end):
            return True
        return False

    def isOverlappingEarlier(self, term):
        if self.earlier_time_Term() < term < self:
            return True
        return False

    def __lt__(self, secondTerm):
        if self.__day.value < secondTerm.__day.value:
            return True
        if self.__day.value > secondTerm.__day.value:
            return False
        if self.__hour < secondTerm.__hour:
            return True
        if self.__hour > secondTerm.__hour:
            return False
        if self.__minute < secondTerm.__minute:
            return True
        if self.__minute > secondTerm.__minute:
            return False
        return False

    def __gt__(self, secondTerm):
        if self.__day.value < secondTerm.__day.value:
            return False
        if self.__day.value > secondTerm.__day.value:
            return True
        if self.__hour < secondTerm.__hour:
            return False
        if self.__hour > secondTerm.__hour:
            return True
        if self.__minute < secondTerm.__minute:
            return False
        if self.__minute > secondTerm.__minute:
            return True
        return False

    def __le__(self, secondTerm):
        return not self.__gt__(secondTerm)

    def __ge__(self, secondTerm):
        return not self.__lt__(secondTerm)

    def __eq__(self, secondTerm):
        return self.equals(secondTerm)

    def __hash__(self):
        return hash(self.__hour + self.minute + self.duration)

    def __sub__(self, secondTerm):
        timeDifference = secondTerm.__duration
        minutesFlag = (self.__minute > secondTerm.__minute)
        hourFlag = (self.__hour > secondTerm.__hour)
        if minutesFlag:
            timeDifference += self.__minute - secondTerm.__minute
        else:
            timeDifference += self.__minute - secondTerm.__minute
        if hourFlag:
            timeDifference += (self.__hour - secondTerm.__hour) * 60
        else:
            timeDifference += (self.__hour - secondTerm.__hour) * 60
        timeDifference += (self.__day.value - secondTerm.__day.value) * 1440
        return Term(secondTerm.__day, secondTerm.__hour, secondTerm.__minute, timeDifference)

    def __add__(self, secondTerm):
        minute = self.__minute + secondTerm.minute
        hour = self.hour + secondTerm.hour
        if minute >= 60:
            minute -= 60
            hour += 1
        if hour >= 24:
            hour -= 24
        return Term(self.day, minute, hour)

    def __str__(self):
        return self.dniTygodnia[self.__day] + " " + str(self.__hour) + ":" + str(self.__minute) + " [" + str(
            self.__duration) + ']'

    def earlierThan(self, termin):
        if self.__hour < termin.__hour:
            return True
        if termin.__hour == self.__hour and self.__minute < termin.__minute:
            return True
        return False

    def laterThan(self, termin):
        return not self.earlierThan(termin)

    def equals(self, termin):
        if termin.__day == self.__day and termin.__hour == self.__hour and termin.__minute == self.__minute and termin.__duration == self.__duration:
            return True
        return False
