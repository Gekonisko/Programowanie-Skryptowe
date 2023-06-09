from Zadanie1 import Operacje
import unittest

class test_decorators(unittest.TestCase):

        
    def testRoznica(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 1)
        self.assertEqual(op.roznica(2), -2)
        self.assertEqual(op.roznica(), 6)
        op['roznica'] = [1, 2, 3]
        self.assertEqual(op.roznica(), 3)
        op['roznica'] = [1, 2, 3, 4]
        self.assertEqual(op.roznica(), 3)

    def testSuma(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2, 3), 6)
        self.assertEqual(op.suma(1, 2), 7)
        self.assertEqual(op.suma(1), 10)
        op['suma'] = [1, 2]
        self.assertEqual(op.suma(1), 4)

    def test__setitem__(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op['suma'] = ['a','b', 'c']

if __name__ == '__main__':
    unittest.main()