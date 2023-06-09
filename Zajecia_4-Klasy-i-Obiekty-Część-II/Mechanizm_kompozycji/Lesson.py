from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term


class Lesson:

    def __init__(self, term, name, teacherName, year):
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__fullTime = False
        if self.is_full_time():
            self.__fullTime = True

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
        return self.__timetable

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
        if self.fullTime:
            if self.__term.day.value < Day.THU.value:
                return True
            if self.__term.day.THU == Day.THU and self.__term.hour <= 16:
                return True
        if not self.__fullTime:
            if self.__term.day == Day.FRI or self.__term.day == Day.SAT:
                return True
        return False

    def earlierDay(self):
        if self.__fullTime:
            if self.__term.day.value > Day.MON.value:
                return True
        if not self.__fullTime:
            if self.__term.day == Day.SAT and 19 >= self.__term.hour >= 17:
                return True
            if self.__term.day == Day.SUN:
                return True
        return False

    def earlierTime(self):
        if self.__fullTime:
            if (self.__term - Term(self.__term.day, 8, 0)).duration > self.__term.duration * 2:
                return True
        if not self.fullTime:
            if self.__term.day == Day.FRI and (
                    self.term - Term(self.__term.day, 17, 0)).duration > self.__term.duration * 2:
                return True
            if (self.__term - Term(self.__term.day, 8, 0)).duration > self.__term.duration * 2:
                return True
        return False

    def laterTime(self):
        if self.__fullTime:
            if self.__term.day.value <= Day.THU.value and (Term(self.__term.day, 20, 0,
                                                                self.__term.duration) - self.__term).duration > self.__term.duration * 2:
                return True
            if self.__term.day == Day.FRI and (Term(self.vterm.day, 17, 0,
                                                    self.__term.duration) - self.__term).duration > self.__term.duration * 2:
                return True
        if not self.__fullTime:
            if (Term(self.__term.day, 20, 0, self.__term.duration) - self.__term).duration > self.__term.duration * 2:
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
