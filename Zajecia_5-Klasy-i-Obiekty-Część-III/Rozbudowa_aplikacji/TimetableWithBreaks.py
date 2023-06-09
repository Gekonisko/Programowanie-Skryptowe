from typing import List
import collections

from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.Mechanizm_hermetyzacji.Action import Action
from Zajecia_4.Mechanizm_hermetyzacji.Lesson import Lesson
from Zajecia_4.Mechanizm_hermetyzacji.TimetableWithoutBreaks import TimetableWithoutBreaks
from Zajecia_5.Klasa_abstrakcyjna.BasicTimetable import BasicTimetable
from Zajecia_5.Rozbudowa_aplikacji.Break import Break


def myFunc(e):
    return e.term


class TimetableWithBreaks(BasicTimetable):
    def __init__(self, breaks: List[Break], skipBreaks: bool):
        self.breaks = breaks
        self.skipBreaks = skipBreaks

    def __str__(self):
        result = (
            f'{" ":15} {"*Poniedziałek":25} {"*Wtorek":25} {"*Środa":25} {"*Czwartek":25} {"*Piątek":25} {"*Sobota":25} {"*Niedziela":25}\n')
        timetable = self.TimeSortedTimetable()
        for key, value in timetable.items():
            startTime = str(value[0].term).split(" ")[1] + " - " + value[0].term.end_time()
            result += f'{startTime:16}'
            for subject in value:
                if subject.__class__ is Break:
                    result += f'*{subject.__str__():25}'*7
                else:
                    for i in range(7):
                        if subject.term.day.value == i:
                            result += f'*{subject.name:25}'
                        else:
                            result += f'{"*":26}'
                result += f'\n{" ":15} {"*" * 175}\n'
        return result

    def put(self, lesson: Lesson) -> bool:
        for key, items in self.TimeSortedTimetable().items():
            for subject in items:
                if subject.term.isOverlappingLater(lesson.term):
                    raise ValueError(f"Nieprawidłowy Termin Zajęć.")
        if not BasicTimetable.Lessons.keys().__contains__(lesson.term):
            BasicTimetable.Lessons[lesson.term] = lesson

    def perform(self, actions: List[Action]):
        for i in range(len(actions)):
            j = i % len(BasicTimetable.Lessons)
            Lessons = BasicTimetable.Lessons
            if Lessons.get(j):
                if actions[i] == Action.DAY_LATER and Lessons.get(j).laterDay():
                    Lessons.get(j).term.day = Day(Lessons.get(j).term.day.value + 1)
                if actions[i] == Action.DAY_EARLIER and Lessons.get(j).earlierDay():
                    Lessons.get(j).term.day = Day(Lessons.get(j).term.day.value - 1)
                if actions[i] == Action.TIME_LATER and Lessons.get(j).laterTime():
                    for _break in self.breaks:
                        if Lessons.get(j).term.isOverlappingLater(_break.term):
                            if self.skipBreaks:
                                Lessons.get(j).term += _break
                            else:
                                raise ValueError("Nieprawidłowy termin")
                    minutes = Lessons.get(j).term.minute + Lessons.get(j).term.duration
                    if minutes >= 60:
                        minutes -= 60
                        Lessons.get(j).term.hour += 1
                    Lessons.get(j).term.minute = minutes
                if actions[i] == Action.TIME_EARLIER and Lessons.get(j).earlierTime():
                    for _break in self.breaks:
                        if Lessons.get(j).term.isOverlappingEarlier(_break.term):
                            if self.skipBreaks:
                                Lessons.get(j).term += _break
                            else:
                                raise ValueError("Nieprawidłowy termin")
                    minutes = Lessons.get(j).term.minute - Lessons.get(j).term.duration
                    if minutes <= 0:
                        minutes = 60 + minutes
                        Lessons.get(j).term.hour -= 1
                    Lessons.get(j).term.minute = minutes

    def TimeSortedTimetable(self):
        timetable = {}
        for key, lesson in TimetableWithBreaks.Lessons.items():
            time = (lesson.term.hour * 60) + lesson.term.minute
            if not timetable.keys().__contains__(time):
                timetable[time] = [lesson]
            else:
                timetable[time].append(lesson)
        for breaks in self.breaks:
            time = (breaks.term.hour * 60) + breaks.term.minute
            if not timetable.keys().__contains__(time):
                timetable[time] = [breaks]
            else:
                timetable[time].append(breaks)
        return collections.OrderedDict(sorted(timetable.items()))

    def isOverlappingBreaks(self, term):
        for _break in self.breaks:
            if term.isOverlapping(_break):
                return True
        return False
