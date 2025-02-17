from parameterized import parameterized
from PyVarTools.math.basic_vars import (
	INFINITY,
	NEGATIVE_INFINITY
)
from unittest import (
	TestCase,
	TestLoader,
	TestSuite,
	TextTestRunner
)


class TestNEGATIVE_INFINITY(TestCase):
	def setUp(self):
		self.neg_inf = NEGATIVE_INFINITY()
	
	def test_abs(self):
		self.assertEqual(abs(self.neg_inf), INFINITY())
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, NEGATIVE_INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(INFINITY(), 0),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_add(self, other, expected):
		self.assertEqual(self.neg_inf + other, expected)
	
	def test_bool(self):
		self.assertFalse(bool(self.neg_inf))
	
	@parameterized.expand([(NEGATIVE_INFINITY(), True), (INFINITY(), False), (1, False),])
	def test_eq(self, other, expected):
		self.assertEqual(self.neg_inf == other, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(-1, INFINITY()),
				(NEGATIVE_INFINITY(), 1),
				(INFINITY(), -1),
			]
	)
	def test_floordiv(self, other, expected):
		self.assertEqual(self.neg_inf // other, expected)
	
	def test_floordiv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.neg_inf // 0
	
	@parameterized.expand(
			[
				(NEGATIVE_INFINITY(), True),
				(INFINITY(), False),
				(1, False),
				(0, False),
				(-1, False),
			]
	)
	def test_ge(self, other, expected):
		self.assertEqual(self.neg_inf >= other, expected)
	
	@parameterized.expand(
			[
				(1, False),
				(0, False),
				(-1, False),
				(INFINITY(), False),
				(NEGATIVE_INFINITY(), False),
			]
	)
	def test_gt(self, other, expected):
		self.assertEqual(self.neg_inf > other, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, NEGATIVE_INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(INFINITY(), 0),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_iadd(self, other, expected):
		self.neg_inf += other
		
		self.assertEqual(self.neg_inf, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(-1, INFINITY()),
				(NEGATIVE_INFINITY(), 1),
				(INFINITY(), -1),
			]
	)
	def test_ifloordiv(self, other, expected):
		self.neg_inf //= other
		
		self.assertEqual(self.neg_inf, expected)
	
	def test_ifloordiv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.neg_inf //= 0
	
	@parameterized.expand([(1, NEGATIVE_INFINITY()), (-1, INFINITY()), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_imod(self, other, expected):
		self.neg_inf %= other
		
		self.assertEqual(self.neg_inf, expected)
	
	def test_imod_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.neg_inf %= 0
	
	@parameterized.expand(
			[
				(2, NEGATIVE_INFINITY()),
				(0.5, NEGATIVE_INFINITY()),
				(0, 0),
				(-2, INFINITY()),
				(-0.5, INFINITY()),
				(NEGATIVE_INFINITY(), INFINITY()),
				(INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_imul(self, other, expected):
		self.neg_inf *= other
		
		self.assertEqual(self.neg_inf, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, 1),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), 0),
				(INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_ipow(self, power, expected):
		self.neg_inf **= power
		
		self.assertEqual(self.neg_inf, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, NEGATIVE_INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(INFINITY(), NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), 0),
			]
	)
	def test_isub(self, other, expected):
		self.neg_inf -= other
		
		self.assertEqual(self.neg_inf, expected)
	
	@parameterized.expand(
			[
				(2, NEGATIVE_INFINITY()),
				(0.5, NEGATIVE_INFINITY()),
				(-2, INFINITY()),
				(-0.5, INFINITY()),
				(NEGATIVE_INFINITY(), 1),
				(INFINITY(), -1),
			]
	)
	def test_itruediv(self, other, expected):
		self.neg_inf /= other
		
		self.assertEqual(self.neg_inf, expected)
	
	def test_itruediv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.neg_inf /= 0
	
	@parameterized.expand([(NEGATIVE_INFINITY(), True), (INFINITY(), True), (1, True), (0, True), (-1, True),])
	def test_le(self, other, expected):
		self.assertEqual(self.neg_inf <= other, expected)
	
	@parameterized.expand([(1, True), (0, True), (-1, True), (INFINITY(), True), (NEGATIVE_INFINITY(), False),])
	def test_lt(self, other, expected):
		self.assertEqual(self.neg_inf < other, expected)
	
	@parameterized.expand([(1, NEGATIVE_INFINITY()), (-1, INFINITY()), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_mod(self, other, expected):
		self.assertEqual(self.neg_inf % other, expected)
	
	def test_mod_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.neg_inf % 0
	
	@parameterized.expand(
			[
				(2, NEGATIVE_INFINITY()),
				(0.5, NEGATIVE_INFINITY()),
				(0, 0),
				(-2, INFINITY()),
				(-0.5, INFINITY()),
				(NEGATIVE_INFINITY(), INFINITY()),
				(INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_mul(self, other, expected):
		self.assertEqual(self.neg_inf * other, expected)
	
	@parameterized.expand([(NEGATIVE_INFINITY(), False), (INFINITY(), True), (1, True),])
	def test_ne(self, other, expected):
		self.assertEqual(self.neg_inf != other, expected)
	
	def test_neg(self):
		self.assertEqual(-self.neg_inf, INFINITY())
	
	def test_pos(self):
		self.assertEqual(+self.neg_inf, NEGATIVE_INFINITY())
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, 1),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), 0),
				(INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_pow(self, power, expected):
		self.assertEqual(self.neg_inf ** power, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, NEGATIVE_INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(INFINITY(), 0),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_radd(self, other, expected):
		self.assertEqual(other + self.neg_inf, expected)
	
	def test_repr(self):
		self.assertEqual(repr(self.neg_inf), "NEGATIVE_INFINITY")
	
	@parameterized.expand([(1, 0), (0, 0), (-1, 0), (NEGATIVE_INFINITY(), 1), (INFINITY(), -1),])
	def test_rfloordiv(self, other, expected):
		self.assertEqual(other // self.neg_inf, expected)
	
	@parameterized.expand([(1, 1), (0, 0), (-1, -1), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_rmod(self, other, expected):
		self.assertEqual(other % self.neg_inf, expected)
	
	@parameterized.expand(
			[
				(2, NEGATIVE_INFINITY()),
				(0.5, NEGATIVE_INFINITY()),
				(0, 0),
				(-2, INFINITY()),
				(-0.5, INFINITY()),
				(NEGATIVE_INFINITY(), INFINITY()),
				(INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_rmul(self, other, expected):
		self.assertEqual(other * self.neg_inf, expected)
	
	def test_round(self):
		self.assertEqual(round(self.neg_inf), NEGATIVE_INFINITY())
		self.assertEqual(round(self.neg_inf, 2), NEGATIVE_INFINITY())
	
	@parameterized.expand([(2, 0), (1, 1), (0, 0), (-1, 0), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_rpow(self, power, expected):
		self.assertEqual(power ** self.neg_inf, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, INFINITY()),
				(-1, INFINITY()),
				(INFINITY(), INFINITY()),
				(NEGATIVE_INFINITY(), 0),
			]
	)
	def test_rsub(self, other, expected):
		self.assertEqual(other - self.neg_inf, expected)
	
	@parameterized.expand([(2, 0), (0.5, 0), (NEGATIVE_INFINITY(), 1), (INFINITY(), -1),])
	def test_rtruediv(self, other, expected):
		self.assertEqual(other / self.neg_inf, expected)
	
	def test_str(self):
		self.assertEqual(str(self.neg_inf), "NEGATIVE_INFINITY")
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, NEGATIVE_INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(INFINITY(), NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), 0),
			]
	)
	def test_sub(self, other, expected):
		self.assertEqual(self.neg_inf - other, expected)
	
	@parameterized.expand(
			[
				(2, NEGATIVE_INFINITY()),
				(0.5, NEGATIVE_INFINITY()),
				(-2, INFINITY()),
				(-0.5, INFINITY()),
				(NEGATIVE_INFINITY(), 1),
			]
	)
	def test_truediv(self, other, expected):
		self.assertEqual(self.neg_inf / other, expected)
	
	def test_truediv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.neg_inf / 0


class TestINFINITY(TestCase):
	def setUp(self):
		self.inf = INFINITY()
	
	def test_abs(self):
		self.assertEqual(abs(self.inf), INFINITY())
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, INFINITY()),
				(-1, INFINITY()),
				(INFINITY(), INFINITY()),
				(NEGATIVE_INFINITY(), 0),
			]
	)
	def test_add(self, other, expected):
		self.assertEqual(self.inf + other, expected)
	
	def test_bool(self):
		self.assertTrue(bool(self.inf))
	
	@parameterized.expand(
			[
				(1, False),
				(0, False),
				(-1, False),
				(INFINITY(), True),
				(NEGATIVE_INFINITY(), False),
			]
	)
	def test_eq(self, other, expected):
		self.assertEqual(self.inf == other, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), -1),
				(INFINITY(), 1),
			]
	)
	def test_floordiv(self, other, expected):
		self.assertEqual(self.inf // other, expected)
	
	def test_floordiv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.inf // 0
	
	@parameterized.expand([(1, True), (0, True), (-1, True), (INFINITY(), True), (NEGATIVE_INFINITY(), True),])
	def test_ge(self, other, expected):
		self.assertEqual(self.inf >= other, expected)
	
	@parameterized.expand([(1, True), (0, True), (-1, True), (INFINITY(), False), (NEGATIVE_INFINITY(), True),])
	def test_gt(self, other, expected):
		self.assertEqual(self.inf > other, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, INFINITY()),
				(-1, INFINITY()),
				(INFINITY(), INFINITY()),
				(NEGATIVE_INFINITY(), 0),
			]
	)
	def test_iadd(self, other, expected):
		self.inf += other
		
		self.assertEqual(self.inf, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), -1),
				(INFINITY(), 1),
			]
	)
	def test_ifloordiv(self, other, expected):
		self.inf //= other
		
		self.assertEqual(self.inf, expected)
	
	def test_ifloordiv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.inf //= 0
	
	@parameterized.expand([(1, INFINITY()), (-1, NEGATIVE_INFINITY()), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_imod(self, other, expected):
		self.inf %= other
		
		self.assertEqual(self.inf, expected)
	
	def test_imod_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.inf %= 0
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, 0),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
				(INFINITY(), INFINITY()),
			]
	)
	def test_imul(self, other, expected):
		self.inf *= other
		
		self.assertEqual(self.inf, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, 1),
				(-1, INFINITY()),
				(NEGATIVE_INFINITY(), 0),
				(INFINITY(), INFINITY()),
			]
	)
	def test_ipow(self, power, expected):
		self.inf **= power
		
		self.assertEqual(self.inf, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, INFINITY()),
				(-1, INFINITY()),
				(INFINITY(), 0),
				(NEGATIVE_INFINITY(), INFINITY()),
			]
	)
	def test_isub(self, other, expected):
		self.inf -= other
		
		self.assertEqual(self.inf, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), -1),
				(INFINITY(), 1),
			]
	)
	def test_itruediv(self, other, expected):
		self.inf /= other
		
		self.assertEqual(self.inf, expected)
	
	def test_itruediv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.inf /= 0
	
	@parameterized.expand(
			[
				(1, False),
				(0, False),
				(-1, False),
				(INFINITY(), True),
				(NEGATIVE_INFINITY(), False),
			]
	)
	def test_le(self, other, expected):
		self.assertEqual(self.inf <= other, expected)
	
	@parameterized.expand(
			[
				(1, False),
				(0, False),
				(-1, False),
				(INFINITY(), False),
				(NEGATIVE_INFINITY(), False),
			]
	)
	def test_lt(self, other, expected):
		self.assertEqual(self.inf < other, expected)
	
	@parameterized.expand([(1, INFINITY()), (-1, NEGATIVE_INFINITY()), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_mod(self, other, expected):
		self.assertEqual(self.inf % other, expected)
	
	def test_mod_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.inf % 0
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, 0),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
				(INFINITY(), INFINITY()),
			]
	)
	def test_mul(self, other, expected):
		self.assertEqual(self.inf * other, expected)
	
	@parameterized.expand([(1, True), (0, True), (-1, True), (INFINITY(), False), (NEGATIVE_INFINITY(), True),])
	def test_ne(self, other, expected):
		self.assertEqual(self.inf != other, expected)
	
	def test_neg(self):
		self.assertEqual(-self.inf, NEGATIVE_INFINITY())
	
	def test_pos(self):
		self.assertEqual(+self.inf, INFINITY())
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, 1),
				(-1, INFINITY()),
				(NEGATIVE_INFINITY(), 0),
				(INFINITY(), INFINITY()),
			]
	)
	def test_pow(self, power, expected):
		self.assertEqual(self.inf ** power, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, INFINITY()),
				(-1, INFINITY()),
				(INFINITY(), INFINITY()),
				(NEGATIVE_INFINITY(), 0),
			]
	)
	def test_radd(self, other, expected):
		self.assertEqual(other + self.inf, expected)
	
	def test_repr(self):
		self.assertEqual(repr(self.inf), "INFINITY")
	
	@parameterized.expand([(1, 0), (-1, 0), (NEGATIVE_INFINITY(), -1), (INFINITY(), 1),])
	def test_rfloordiv(self, other, expected):
		self.assertEqual(other // self.inf, expected)
	
	@parameterized.expand([(1, 1), (0, 0), (-1, -1), (NEGATIVE_INFINITY(), 0), (INFINITY(), 0),])
	def test_rmod(self, other, expected):
		self.assertEqual(other % self.inf, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, 0),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
				(INFINITY(), INFINITY()),
			]
	)
	def test_rmul(self, other, expected):
		self.assertEqual(other * self.inf, expected)
	
	def test_round(self):
		self.assertEqual(round(self.inf), INFINITY())
		self.assertEqual(round(self.inf, 2), INFINITY())
	
	@parameterized.expand(
			[
				(2, INFINITY()),
				(1, 1),
				(0, 0),
				(-1, INFINITY()),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
				(INFINITY(), INFINITY()),
			]
	)
	def test_rpow(self, power, expected):
		self.assertEqual(power ** self.inf, expected)
	
	@parameterized.expand(
			[
				(1, NEGATIVE_INFINITY()),
				(0, NEGATIVE_INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(INFINITY(), 0),
				(NEGATIVE_INFINITY(), NEGATIVE_INFINITY()),
			]
	)
	def test_rsub(self, other, expected):
		self.assertEqual(other - self.inf, expected)
	
	@parameterized.expand([(1, 0), (-1, 0), (NEGATIVE_INFINITY(), -1), (INFINITY(), 1),])
	def test_rtruediv(self, other, expected):
		self.assertEqual(other / self.inf, expected)
	
	def test_str(self):
		self.assertEqual(str(self.inf), "INFINITY")
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(0, INFINITY()),
				(-1, INFINITY()),
				(INFINITY(), 0),
				(NEGATIVE_INFINITY(), INFINITY()),
			]
	)
	def test_sub(self, other, expected):
		self.assertEqual(self.inf - other, expected)
	
	@parameterized.expand(
			[
				(1, INFINITY()),
				(-1, NEGATIVE_INFINITY()),
				(NEGATIVE_INFINITY(), -1),
				(INFINITY(), 1),
			]
	)
	def test_truediv(self, other, expected):
		self.assertEqual(self.inf / other, expected)
	
	def test_truediv_zero_error(self):
		with self.assertRaises(ZeroDivisionError):
			self.inf / 0


def basic_vars_test_suite() -> TestSuite:
	suite = TestSuite()
	test_loader = TestLoader()
	
	suite.addTest(test_loader.loadTestsFromTestCase(TestINFINITY))
	suite.addTest(test_loader.loadTestsFromTestCase(TestNEGATIVE_INFINITY))
	
	return suite


if __name__ == "__main__":
	runner = TextTestRunner()
	runner.run(basic_vars_test_suite())
