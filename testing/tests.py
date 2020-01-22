import unittest
import basic_tests


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(basic_tests)
    # suite.addTests(unittest.TestLoader().loadTestsFromModule(tests_best_fit_curves))

    unittest.TextTestRunner(verbosity=2).run(suite)
