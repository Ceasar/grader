import sys
import unittest


class Problem(object):
  """A Problem that can be graded."""
  def __init__(self, test_case, weights):
    assert all(test_name in test_case.__dict__ for test_name in weights)
    assert all(weight > 0 for weight in weights.values())
    self._test_case = test_case
    self.weights = weights #test_name -> weight map

  @property
  def max_grade(self):
    return sum(self.weights.values())

  @property
  def results(self):
    for test_name, weight in self.weights.items():
      test = self._get_test_from_test_name(test_name)
      result = unittest.TestResult()
      test.run(result)
      yield test_name, weight, result

  @property
  def grade(self):
    final_score = 0
    for _, weight, result in self.results:
      if result.wasSuccessful():
        final_score += weight
    return final_score

  def _get_test_from_test_name(self, test_name):
    return self._test_case(test_name)

  def print_results(self):
    """Print the results of the tests and the grade for the problem."""
    print "Grading %s..." % self._test_case
    for test_name, weight, result in self.results:
      print "Running %s..." % test_name
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
      total += problem.grade
      max_pt += problem.max_grade
      problem.print_results()
    print "Final Grade: %d/%d" % (total, max_pt)
