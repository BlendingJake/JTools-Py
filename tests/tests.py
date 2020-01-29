import unittest
import filter_tests
import getter_tests
import formatter_tests


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(filter_tests)
    suite.addTests(unittest.TestLoader().loadTestsFromModule(getter_tests))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(formatter_tests))

    unittest.TextTestRunner(verbosity=2).run(suite)
