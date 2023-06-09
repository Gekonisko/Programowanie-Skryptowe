import unittest
from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term
from Zajecia_4.Mechanizm_hermetyzacji.Action import Action
from Zajecia_4.Mechanizm_kompozycji.Lesson import Lesson
from Zajecia_5.Rozbudowa_aplikacji.Break import Break
from Zajecia_5.Rozbudowa_aplikacji.TimetableWithBreaks import TimetableWithBreaks


class Test_TimetableWithBreaks(unittest.TestCase):

    def test(self):
        lesson1 = Lesson(Term(Day.TUE, 16, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.SUN, 18, 0), "Zajecia Niestacjonarne", "Profesor Niestacjonarny", 3)
        break1 = Break(Term(day=Day.TUE, hour=10, minute=0, duration=15))
        break2 = Break(Term(day=Day.TUE, hour=9, minute=30, duration=10))
        break3 = Break(Term(day=Day.TUE, hour=11, minute=10, duration=10))
        timeTable = TimetableWithBreaks([break1, break2, break3], True)
        timeTable.put(lesson1)

        timeTable.put(lesson2)
        actions = timeTable.parse(['t-', 'd-', 't+', 'd-'])
        self.assertEqual(
            actions.__eq__([Action.TIME_EARLIER, Action.DAY_EARLIER, Action.TIME_LATER, Action.DAY_EARLIER]), True)
        timeTable.perform(actions)
        print(timeTable)


if __name__ == '__main__':
    unittest.main()
    unittest.main()
