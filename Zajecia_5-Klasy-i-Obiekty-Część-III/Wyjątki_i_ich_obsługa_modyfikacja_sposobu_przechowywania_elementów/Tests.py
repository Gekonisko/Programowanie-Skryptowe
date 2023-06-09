import unittest
from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term
from Zajecia_4.Mechanizm_kompozycji.Lesson import Lesson
from Zajecia_5.Rozbudowa_aplikacji.TimetableWithBreaks import TimetableWithBreaks


class Test_TimetableWithBreaksErrors(unittest.TestCase):

    def test(self):
        lesson1 = Lesson(Term(Day.TUE, 9, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.TUE, 9, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        timeTable = TimetableWithBreaks([], True)
        timeTable.put(lesson1)
        timeTable.put(lesson2)
        actions = timeTable.parse(['t-', 'd-', 't+', 'd-'])
        timeTable.perform(actions)
        print(timeTable)


if __name__ == '__main__':
    unittest.main()
    unittest.main()
