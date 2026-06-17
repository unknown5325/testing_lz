import unittest
from testing import task1


a1 = task1(13, 4, 4, 1)
a2 = task1(67, 42, 6, 1)
a3 = task1(13, 4, 4, True)
a4 = task1(13, 4, 4, '1')

class Testingg(unittest.TestCase):
    def test_t1(self):
        self.assertEqual(a1, a2)

    def test_t2(self):
        self.assertEqual(a1, a3)

    def test_t3(self):
        self.assertEqual(a1, a4)

    def test_t4(self):
        self.assertRaises(ValueError, task1, 8, 5, 4, 'feqfw')
    
    def test_t5(self):
        self.assertRaises(ZeroDivisionError, task1, 8, 5, 4, 4)

    def test_t6(self):
        self.assertRaises(ValueError, task1, 8, 15, 7, 4)

    def test_t7(self):
        self.assertRaises(ValueError, task1, 10**900, 5, 9, 4)


if __name__ == "__main__":
    unittest.main()