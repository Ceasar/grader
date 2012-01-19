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

Running the code above in my project outputs the following text:

    02:11:12 ~/hw1$ python tests.py
    ======================================================================
    Grading <class '__main__.SortedListTestCase'>...
    Running test_extend...
    Points: 5/5
    Running test_append...
    Points: 5/5
    Running test_setitem...
    Points: 5/5
    ======================================================================
    Grading <class '__main__.InvertDictTestCase'>...
    Running test_new_keys_are_old_values...
    Points: 5/5
    Running test_new_values_are_old_keys...
    Points: 5/5
    Running test_new_keys_are_old_values2...
    Points: 5/5
    Running test_new_values_are_old_keys2...
    Points: 5/5
    ======================================================================
    Grading <class '__main__.ConcordanceTestCase'>...
    Running test_bad_lookup3...
    Points: 5/5
    Running test_bad_lookup2...
    Points: 5/5
    Running test_bad_lookup1...
    Points: 5/5
    Running test_bad_input...
    Points: 5/5
    Running test_lookup3...
    Points: 5/5
    Running test_lookup2...
    Points: 5/5
    Running test_lookup1...
    Points: 5/5
    Running test_lookup7...
    Points: 10/10
    Running test_lookup6...
    Points: 5/5
    Running test_lookup5...
    Points: 10/10
    Running test_lookup4...
    Points: 5/5
    ======================================================================
    Final Grade: 100/100

Changing the look of the output
-------------------------------

The output is admittedly rather simple and straightforward. Fortunately, changing it is pretty easy. Just extend Problem or Grader and override the *print_results* method as desired.

Contributors
============

* Ceasar Bautista cbautista2010@gmail.com
