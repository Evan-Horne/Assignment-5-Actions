import unittest
import task
import math
from datetime import date


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testArea(self):
        expected = math.pi
        self.assertAlmostEqual(expected, task.circleArea(1))

    def testFirstAndLast(self):
        arr = ["first", "middle", "last"]
        first, last = task.firstAndLast(arr)
        self.assertEqual(first, "first")
        self.assertEqual(last, "last")

    def testNumDays(self):
        f_date = date(2014, 7, 2)
        l_date = date(2014, 7, 11)
        self.assertEqual(9, task.numDays(f_date, l_date))


if __name__ == "__main__":
    unittest.main()
