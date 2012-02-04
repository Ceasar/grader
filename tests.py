import time
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        """Make sure the shuffled sequence does not lose any elements"""
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        """Make sure random.choice picks an element in a given sequence."""
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        """Make sure random.sample picks items only from the given sequence."""
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    def test_sleep(self):
        """Make sure to print the name of a test before it starts running."""
        time.sleep(3)
        self.assertTrue(True)

    def test_no_docstring(self):
        # no docstring should be printed
        self.assertTrue(True)

    def test_unused(self):
        # this test should never be run
        self.assertTrue(True)


if __name__ == "__main__":
    from grader import Problem, Grader
    problem1 = Problem(TestSequenceFunctions, [
      ('test_shuffle', 4),
      ('test_choice', 2),
      ('test_sample', 4),
      ('test_sleep', 5),
      ('test_no_docstring', 5),
      ])
    grader = Grader([problem1])
    grader.print_results()
