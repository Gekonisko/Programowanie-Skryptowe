import unittest
from DeanerySystem.Day import Day, nthDayFrom
from DeanerySystem.Term import Term


class Test_Temp(unittest.TestCase):

    def test(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        self.assertEqual(term1.__str__(), "Wtorek 9:45 [90]")
        self.assertEqual(term2.__str__(), "Środa 10:15 [90]")
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term1.equals(term2), False)


if __name__ == '__main__':
    unittest.main()
