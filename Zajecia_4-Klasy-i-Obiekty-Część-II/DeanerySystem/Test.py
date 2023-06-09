import unittest
from Zajecia_4.DeanerySystem.Day import Day, nthDayFrom
from Zajecia_4.DeanerySystem.Term import Term


class Test_Temp(unittest.TestCase):

    def test(self):
        term1 = Term(Day.MON, 8, 30)
        term2 = Term(Day.TUE, 9, 45, 30)
        term3 = Term(Day.TUE, 9, 45, 90)
        self.assertEqual(term1 < term2, True)
        self.assertEqual(term1 <= term2, True)
        self.assertEqual(term1 > term2, False)
        self.assertEqual(term1 >= term2, False)
        self.assertEqual(term2 == term2, True)
        self.assertEqual(term2 == term3, False)
        self.assertEqual((term3 - term1).__str__(), "Poniedziałek 8:30 [1605]")


if __name__ == '__main__':
    unittest.main()
