from typing import List

from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term
from Zajecia_4.Mechanizm_hermetyzacji.Action import Action
from Zajecia_4.Mechanizm_kompozycji.Lesson import Lesson
from Zajecia_5.Klasa_abstrakcyjna.BasicTimetable import BasicTimetable


def myFunc(e):
    return e.term


class TimetableWithoutBreaks(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """

    def __str__(self):
        result = (
            f'{" ":15} {"*Poniedziałek":25} {"*Wtorek":25} {"*Środa":25} {"*Czwartek":25} {"*Piątek":25} {"*Sobota":25} {"*Niedziela":25}\n')

        for lesson in BasicTimetable.Lessons:
            time = str(lesson.term).split(" ")[1] + " - " + lesson.term.end_time()
            result += f'{time:16}'
            for i in range(7):
                if lesson.term.day.value == i:
                    result += f'*{lesson.name:25}'
                else:
                    result += f'{"*":26}'
            result += f'\n{" ":15} {"*" * 175}\n'
        return result

    ##########################################################
    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:
        if fullTime:
            if Term(Day.MON, 8, 0) <= term < Term(Day.MON, 20, 0):
                return True
            if Term(Day.TUE, 8, 0) <= term < Term(Day.TUE, 20, 0):
                return True
            if Term(Day.WED, 8, 0) <= term < Term(Day.WED, 20, 0):
                return True
            if Term(Day.THU, 8, 0) <= term < Term(Day.THU, 20, 0):
                return True
            if Term(Day.FRI, 8, 0) <= term < Term(Day.FRI, 17, 0):
                return True
        if not fullTime:
            if Term(Day.FRI, 17, 0) <= term < Term(Day.FRI, 20, 0):
                return True
            if Term(Day.SAT, 8, 0) <= term < Term(Day.SAT, 20, 0):
                return True
            if Term(Day.SUN, 8, 0) <= term < Term(Day.SUN, 20, 0):
                return True
        return False

    ##########################################################

    def put(self, lesson: Lesson) -> bool:
        if not BasicTimetable.Lessons.__contains__(Lesson):
            BasicTimetable.Lessons.append(lesson)
            BasicTimetable.Lessons.sort(key=myFunc)

    ##########################################################

    def perform(self, actions: List[Action]):
        for i in range(len(actions)):
            j = i % len(BasicTimetable.Lessons)
            if BasicTimetable.Lessons[j]:
                if actions[i] == Action.DAY_LATER and BasicTimetable.Lessons[j].laterDay():
                    BasicTimetable.Lessons[j].term.day = Day(BasicTimetable.Lessons[j].term.day.value + 1)
                if actions[i] == Action.DAY_EARLIER and BasicTimetable.Lessons[j].earlierDay():
                    BasicTimetable.Lessons[j].term.day = Day(BasicTimetable.Lessons[j].term.day.value - 1)
                if actions[i] == Action.TIME_LATER and BasicTimetable.Lessons[j].laterTime():
                    minutes = BasicTimetable.Lessons[j].term.minute + BasicTimetable.Lessons[j].term.duration
                    if minutes >= 60:
                        minutes -= 60
                        BasicTimetable.Lessons[j].term.hour += 1
                    BasicTimetable.Lessons[j].term.minute = minutes
                if actions[i] == Action.TIME_EARLIER and BasicTimetable.Lessons[j].earlierTime():
                    minutes = BasicTimetable.Lessons[j].term.minute - BasicTimetable.Lessons[j].term.duration
                    if minutes <= 0:
                        minutes = 60 + minutes
                        BasicTimetable.Lessons[j].term.hour -= 1
                    BasicTimetable.Lessons[j].term.minute = minutes

