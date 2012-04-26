"""Grading system based on unittest test cases."""

import threading
import unittest


class Problem(object):
    """A Problem that can be graded.

    test_case should be an instance of unittest.TestCase

    test_weights should be a list of test_name-weight pairs.

    timeout should be the time to wait before killing a test, specified in
    seconds. By default, timeout is None and the test will wait until
    completion."""

    def __init__(self, test_case, test_weights, timeout=None):
        assert all(test in test_case.__dict__ for test, _ in test_weights)
        assert all(weight > 0 for _, weight in test_weights)
        self.test_weights = test_weights
        self.timeout = timeout
        self._test_case = test_case
        self._results = {}    # test_name -> result

    @property
    def max_grade(self):
        """The maxiumum grade possible for the problem."""
        return sum(weight for _, weight in self.test_weights)

    def _get_test_from_test_name(self, test_name):
        """Return the test with the given name."""
        return self._test_case(test_name)

    def result(self, test_name):
        """Return the result for the given test."""
        try:
            return self._results[test_name]
        except KeyError:
            test = self._get_test_from_test_name(test_name)
            result = unittest.TestResult()
            test_runner = threading.Thread(target=test.run, args=(result,))
            test_runner.daemon = True
            test_runner.start()

            test_runner.join(self.timeout)

            # if the test is still running, report a failure
            if test_runner.isAlive():
                result.addFailure(test, (RuntimeError, "Time out", ""))

            self._results[test_name] = result
            return result

    @property
    def grade(self):
        """Grade earned for the problem."""
        return sum(weight for test, weight in self.test_weights \
                if self.result(test).wasSuccessful())

    def print_results(self):
        """Print the results of the tests and the grade for the problem."""
        print "Grading %s..." % self._test_case
        for test_name, weight in self.test_weights:
            print "Running %s..." % test_name
            test = self._get_test_from_test_name(test_name)
            if test.shortDescription():
                print test.shortDescription()
            result = self.result(test_name)
            if result.wasSuccessful():
                print "Points: %d/%d" % (weight, weight)
            else:
                print "-" * 70
                # legacy code. not sure what exactly is happening here
                try:
                    print result.errors[0][1]
                except IndexError:
                    pass
                try:
                    print result.failures[0][1]
                except IndexError:
                    pass
                print "Points: 0/%d" % weight
                print "-" * 70
        print "=" * 70


class Grader(object):
    """A grader object."""
    def __init__(self, problems):
        self.problems = problems

    def print_results(self):
        """Grade each problem and print out the final grade."""
        print "=" * 70
        total, max_pt = 0, 0
        for problem in self.problems:
            problem.print_results()
            total += problem.grade
            max_pt += problem.max_grade
        print "Final Grade: %d/%d" % (total, max_pt)
