import unittest
from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term
from Zajecia_4.Mechanizm_hermetyzacji.Action import Action
from Zajecia_4.Mechanizm_hermetyzacji.TimetableWithoutBreaks import TimetableWithoutBreaks
from Zajecia_4.Mechanizm_kompozycji.Lesson import Lesson


class Test_TimetableWithoutBreaks(unittest.TestCase):

    def test(self):
        lesson1 = Lesson(Term(Day.TUE, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.SUN, 18, 0), "Zajecia Niestacjonarne", "Profesor Niestacjonarny", 3)
        TimetableWithoutBreaks().put(lesson2)
        TimetableWithoutBreaks().put(lesson1)
        print(TimetableWithoutBreaks())
        self.assertEqual(TimetableWithoutBreaks().can_be_transferred_to(Term(Day.SUN, 8, 0), True), False)
        self.assertEqual(TimetableWithoutBreaks().can_be_transferred_to(Term(Day.SUN, 10, 0), False), True)
        self.assertEqual(TimetableWithoutBreaks().busy(Term(Day.TUE, 8, 0)), True)
        self.assertEqual(TimetableWithoutBreaks().busy(Term(Day.SUN, 18, 0)), True)
        actions = TimetableWithoutBreaks().parse(['t-', 'd-', 't+', 'd-'])
        self.assertEqual(actions.__eq__([Action.TIME_EARLIER, Action.DAY_EARLIER, Action.TIME_LATER, Action.DAY_EARLIER]), True)
        TimetableWithoutBreaks().perform(actions)
        self.assertEqual(TimetableWithoutBreaks().busy(Term(Day.TUE, 8, 0)), True)
        self.assertEqual(TimetableWithoutBreaks().busy(Term(Day.SUN, 18, 0)), True)
        self.assertEqual(TimetableWithoutBreaks().get(Term(Day.SUN, 18, 0)), None)
        print(TimetableWithoutBreaks())



if __name__ == '__main__':
    unittest.main()
    unittest.main()
