import unittest
import task
import math


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


if __name__ == "__main__":
    unittest.main()
