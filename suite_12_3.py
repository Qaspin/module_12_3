import unittest
from tests_12_3 import RunnerTest, TournamentTest

TSuite = unittest.TestSuite()
TSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
TSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TSuite)