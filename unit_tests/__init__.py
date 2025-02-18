from unit_tests.math import math_test_suite
from unittest import (
	TestSuite,
	TextTestRunner
)


def main_test_suite() -> TestSuite:
	suite = TestSuite()
	
	suite.addTest(math_test_suite())
	
	return suite


if __name__ == "__main__":
	runner = TextTestRunner()
	runner.run(main_test_suite())
