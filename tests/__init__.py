import unittest
from . import filter_tests
from . import getter_tests
from . import formatter_tests
from . import performance_tests


def run_tests():
    suite = unittest.TestLoader().loadTestsFromModule(filter_tests)
    suite.addTests(unittest.TestLoader().loadTestsFromModule(getter_tests))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(formatter_tests))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(performance_tests))

    return suite