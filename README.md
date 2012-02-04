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
      problem1 = Problem(TestSequenceFunctions, [
        ('test_shuffle', 4),
        ('test_choice', 2),
        ('test_sample', 4),
        ('test_sleep', 5),
        ])
      grader = Grader([problem1])
      grader.print_results()

Running the code above in my project outputs the following text:

    19:53:53 ~/grader$ python tests.py
    ======================================================================
    Grading <class '__main__.TestSequenceFunctions'>...
    Running test_shuffle...
    Points: 4/4
    Running test_choice...
    Points: 2/2
    Running test_sleep...
    Points: 5/5
    Running test_sample...
    Points: 4/4
    ======================================================================
    Final Grade: 15/15

Changing the look of the output
-------------------------------

The output is admittedly rather simple and straightforward. Fortunately, changing it is pretty easy. Just extend Problem or Grader and override the *print_results* method as desired.

Contributors
============

* Ceasar Bautista cbautista2010@gmail.com
