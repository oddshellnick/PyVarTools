from unit_tests.math import math_test_suite
from unittest import (
	TestSuite,
	TextTestRunner
)
from unit_tests.python_instances_tools import python_instances_tools_test_suite

def main_test_suite() -> TestSuite:
	suite = TestSuite()
	
	suite.addTest(math_test_suite())
	suite.addTest(python_instances_tools_test_suite())
	
	return suite


if __name__ == "__main__":
	runner = TextTestRunner()
	runner.run(main_test_suite())
