from abc import ABC, abstractmethod
from typing import List

from Zajecia_4.Mechanizm_hermetyzacji.Action import Action
from Zajecia_4.Mechanizm_hermetyzacji.Lesson import Lesson
from Zajecia_5.Mechanizm_dziedziczenia.Term import Term


class BasicTimetable(ABC):
    Lessons = {}


    @abstractmethod
    def perform(self, actions):
        pass

    @abstractmethod
    def put(self, lesson: Lesson) -> bool:
        pass

    def busy(self, term: Term) -> bool:
        if not BasicTimetable.Lessons.keys().__contains__(term):
            return False
        return True

    def get(self, term: Term) -> Lesson:
        for lesson in BasicTimetable.Lessons:
            if lesson.term == term:
                return lesson
        return None

    def parse(self, actions: List[str]) -> List[Action]:
        result = []
        for action in actions:
            if action == "d-":
                result.append(Action.DAY_EARLIER)
            elif action == "d+":
                result.append(Action.DAY_LATER)
            elif action == "t-":
                result.append(Action.TIME_EARLIER)
            elif action == "t+":
                result.append(Action.TIME_LATER)
            else:
                raise ValueError(f"Translation {action} is incorrect")
        return result