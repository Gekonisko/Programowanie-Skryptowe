import unittest
from Zajecia_4.DeanerySystem.Day import Day
from Zajecia_4.DeanerySystem.Term import Term
from Zajecia_4.Mechanizm_hermetyzacji.TimetableWithoutBreaks import TimetableWithoutBreaks
from Zajecia_4.Mechanizm_kompozycji.Lesson import Lesson


class Test_Lesson(unittest.TestCase):

    def test(self):
        lesson1 = Lesson(Term(Day.TUE, 8, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.SUN, 19, 0), "Zajecia Niestacjonarne", "Profesor Niestacjonarny", 3)
        self.assertEqual(lesson1.fullTime, True)
        self.assertEqual(lesson2.fullTime, False)
        self.assertEqual(lesson1.laterDay(), True)
        self.assertEqual(lesson2.laterDay(), False)
        self.assertEqual(lesson1.earlierDay(), True)
        self.assertEqual(lesson2.earlierDay(), True)
        self.assertEqual(lesson1.laterTime(), True)
        self.assertEqual(lesson2.laterTime(), False)
        self.assertEqual(lesson1.earlierTime(), False)
        self.assertEqual(lesson2.earlierTime(), True)

if __name__ == '__main__':
    unittest.main()
    unittest.main()
