from unit_tests.math.vars import vars_test_suite
from unittest import (
	TestSuite,
	TextTestRunner
)
from unit_tests.math.basic_vars import basic_vars_test_suite


def math_test_suite() -> TestSuite:
	suite = TestSuite()
	
	suite.addTest(basic_vars_test_suite())
	suite.addTest(vars_test_suite())
	
	return suite


if __name__ == "__main__":
	runner = TextTestRunner()
	runner.run(math_test_suite())
