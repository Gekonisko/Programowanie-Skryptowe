from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term


class Lesson:

    def __int__(self, timetable, term, name, teacherName, year):
        self.__timetable = timetable
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = False
        if self.is_full_time():
            self.__fullTime = True

    @property
    def term(self):
        return self.__term

    @property
    def name(self):
        return self.__name

    @property
    def teacherName(self):
        return self.__teacherName

    @property
    def year(self):
        return self.__year

    @property
    def fullTime(self):
        return self.__fullTime

    @term.setter
    def term(self, var):
        self.__term = var

    @name.setter
    def name(self, var):
        self.__name = var

    @teacherName.setter
    def teacherName(self, var):
        self.__teacherName = var

    @year.setter
    def year(self, var):
        self.__year = var

    @fullTime.setter
    def fullTime(self, var):
        self.__fullTime = var

    def laterDay(self):
        newTerm = Term(Day((self.__term.day.value + 1) % 7), self.__term.hour, self.__term.minute, self.__term.duration)
        if self.__timetable.can_be_transferred_to(newTerm, self.__fullTime):
            return True
        return False

    def earlierDay(self):
        newTerm = Term(Day((self.__term.day.value - 1) % 7), self.__term.hour, self.__term.minute, self.__term.duration)
        if self.__timetable.can_be_transferred_to(newTerm, self.__fullTime):
            return True
        return False

    def earlierTime(self):
        minutes = self.__term.minute - self.__term.duration
        hour = self.__term.hour
        if minutes <= 0:
            minutes += 60
            hour -= 1
        newTerm = Term(self.__term.day, hour, minutes, self.__term.duration)
        if self.__timetable.can_be_transferred_to(newTerm):
            return True
        return False

    def laterTime(self):
        minutes = self.__term.minute - self.__term.duration
        hour = self.__term.hour
        if minutes >= 0:
            minutes -= 60
            hour += 1
        newTerm = Term(self.__term.day, hour, minutes, self.__term.duration)
        if self.__timetable.can_be_transferred_to(newTerm):
            return True
        return False

    def is_full_time(self):
        if Term(Day.MON, 8, 0) <= self.__term < Term(Day.MON, 20, 0):
            return True
        if Term(Day.TUE, 8, 0) <= self.__term < Term(Day.TUE, 20, 0):
            return True
        if Term(Day.WED, 8, 0) <= self.__term < Term(Day.WED, 20, 0):
            return True
        if Term(Day.THU, 8, 0) <= self.__term < Term(Day.THU, 20, 0):
            return True
        if Term(Day.FRI, 8, 0) <= self.__term < Term(Day.FRI, 17, 0):
            return True

    def year_str(self):
        y = "Piąty"
        if self.__year == 1:
            y = "Pierwszy"
        elif self.__year == 2:
            y = "Drugi"
        elif self.__year == 3:
            y = "Trzeci"
        elif self.__year == 4:
            y = "Czwarty"
        s = "stacjonarnych"
        if self.__fullTime == False:
            s = "niestacjonarnych"
        return y + " rok studiów " + s

    def __str__(self):
        return self.__name + "(" + self.__term.__str__() + ") \n" \
               + self.__year_str() + "\n" \
               + "Prowadzący: " + self.__teacherName
