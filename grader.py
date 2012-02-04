import unittest


class Problem(object):
  """A Problem that can be graded."""
  def __init__(self, test_case, test_weights):
    assert all(test in test_case.__dict__ for test, _ in test_weights)
    assert all(weight > 0 for _, weight in test_weights)
    self.test_weights = test_weights
    self._test_case = test_case
    self._results = {}  # test_name -> result

  @property
  def max_grade(self):
    return sum(weight for _, weight in self.test_weights)

  def _get_test_from_test_name(self, test_name):
    return self._test_case(test_name)

  def result(self, test_name):
    try:
      return self._results[test_name]
    except KeyError:
      test = self._get_test_from_test_name(test_name)
      result = unittest.TestResult()
      test.run(result)
      self._results[test_name] = result
      return result

  @property
  def grade(self):
    return sum(weight for test, weight in self.test_weights \
        if self.result(test).wasSuccessful())

  def print_results(self):
    """Print the results of the tests and the grade for the problem."""
    print "Grading %s..." % self._test_case
    for test_name, weight in self.test_weights:
      print "Running %s..." % test_name
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
