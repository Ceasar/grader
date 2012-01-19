Basic info
==========

Grader is a tool for grading Python assignments. It builds off of unittest so
no dependencies are required.

More info
==========

grader.py consists of two classes, Problem and Grader. A Grader simply
aggregates problems and their grades. Problems are where all the real work
happens.

A Problem wraps a unittest.TestCase and takes a dictionary of weights for
each unittest within the TestCase. It supports several queries for information
about the graded solution and a method to print the results.

Usage
==========

Using Grader is pretty effortless.

In your tests.py file, import Grader and Problem from grader.py.

Then, at the bottom of your file, replace unittest.main() with something like
the following:

    if __name__ == "__main__":
      from grader import Problem, Grader
      problem1 = Problem(SortedListTestCase, {
        'test_append': 5,
        'test_extend': 5,
        'test_setitem': 5
        })
      problem2 = Problem(InvertDictTestCase, {
        'test_new_keys_are_old_values': 5,
        'test_new_values_are_old_keys': 5,
        'test_new_keys_are_old_values2': 5,
        'test_new_values_are_old_keys2': 5
        })
      problem3 = Problem(ConcordanceTestCase, {
        'test_bad_input': 5,
        'test_bad_lookup1': 5,
        'test_bad_lookup2': 5,
        'test_bad_lookup3': 5,
        'test_lookup1': 5,
        'test_lookup2': 5,
        'test_lookup3': 5,
        'test_lookup4': 5,
        'test_lookup5': 10,
        'test_lookup6': 5,
        'test_lookup7': 10
        })
      grader = Grader([problem1, problem2, problem3])
      grader.print_results()
