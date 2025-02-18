class INFINITY:
	"""
	Represents positive infinity in a simplified numerical system.

	This class is designed to mimic the behavior of positive infinity in basic numerical operations,
	within a simplified framework that prioritizes practical utility over strict mathematical rigor.
	It treats positive infinity as an unbounded value greater than any finite number, but simplifies
	operations with indeterminate forms to provide concrete, though not always mathematically
	definitive, results.

	**Key Simplifications and Concepts:**

	- **Simplified Infinity:** `INFINITY` is not intended as a mathematically rigorous
	  representation of infinity. Instead, it behaves like an extremely large positive number
	  for practical purposes within this simplified system.

	- **Indeterminate Forms:** Operations that result in mathematically indeterminate forms
	  (like `+∞ - ∞`, `+∞ / +∞`, `+∞ * 0`, `+∞ / -∞`, etc.) are simplified to return
	  specific concrete values (often 0, 1, or -1) for ease of use in programmatic contexts,
	  rather than raising errors or returning NaN-like values. These simplifications are design choices
	  to provide a usable, albeit not strictly mathematically accurate, infinity representation.

	- **Basic Arithmetic:** Standard arithmetic operations are overloaded to behave consistently with the intuitive understanding of positive infinity, such as:

		- `+∞ + x = +∞` for any finite number `x`
		- `+∞ * x = +∞` for `x > 0`
		- `+∞ * x = -∞` for `x < 0`
		- `+∞ / x = +∞` for `x > 0`
		- `+∞ / x = -∞` for `x < 0`
		- `x / +∞ = 0` for any finite number `x`
		- `(+∞) ** x = +∞` for most positive powers `x`
		- `x ** (+∞) = +∞` for `x > 1`
		- `(+∞) ** 0 = 1` (simplified interpretation for this system)

	- **Comparisons:** Comparisons are designed to reflect positive infinity as the largest value:

		- `+∞ > x` is always true for any value `x` not equal to `+∞`
		- `+∞ < x` is always false for any value `x`
		- `+∞ >= x` is always true
		- `+∞ <= x` is true only if `x` is also `+∞`

	- **Boolean Value:** `bool(INFINITY)` is defined as `True`.

	**Use Case:**

	This class is useful in scenarios where you need to represent and operate with the concept of
	positive infinity in a program, but strict mathematical accuracy for all edge cases and
	indeterminate forms is not critical. It provides a pragmatic approach for handling
	infinite bounds or values in algorithms and calculations where a simplified infinite value is sufficient.

	**Important Note:** For applications requiring rigorous mathematical correctness with infinities,
	especially in symbolic computations or advanced numerical analysis, a more sophisticated
	representation and handling of indeterminate forms would be necessary. This class is a
	practical simplification, not a complete mathematical model.
	"""
	
	def __str__(self):
		return "INFINITY"
	
	def __repr__(self):
		return "INFINITY"
	
	def __abs__(self):
		return self
	
	def __bool__(self):
		return True
	
	def __ge__(self, other):
		return True
	
	def __eq__(self, other):
		return isinstance(other, INFINITY)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __gt__(self, other):
		return self.__ne__(other)
	
	def __add__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 0
		
		return self
	
	def __iadd__(self, other):
		return self.__add__(other)
	
	def __floordiv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return -1
		
		if isinstance(other, INFINITY):
			return 1
		
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			raise ZeroDivisionError
		
		return self
	
	def __ifloordiv__(self, other):
		return self.__floordiv__(other)
	
	def __mod__(self, other):
		if isinstance(other, (INFINITY, NEGATIVE_INFINITY)):
			return 0
		
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			raise ZeroDivisionError
		
		return self
	
	def __imod__(self, other):
		return self.__mod__(other)
	
	def __mul__(self, other):
		if isinstance(other, (int, float, NEGATIVE_INFINITY)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			return 0
		
		return self
	
	def __imul__(self, other):
		return self.__mul__(other)
	
	def __pow__(self, power, modulo=None):
		if isinstance(power, NEGATIVE_INFINITY):
			return 0
		
		if power == 0:
			return 1
		
		return self
	
	def __ipow__(self, power, modulo=None):
		return self.__pow__(power, modulo)
	
	def __sub__(self, other):
		if isinstance(other, INFINITY):
			return 0
		
		return self
	
	def __isub__(self, other):
		return self.__sub__(other)
	
	def __truediv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return -1
		
		if isinstance(other, INFINITY):
			return 1
		
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			raise ZeroDivisionError
		
		return self
	
	def __itruediv__(self, other):
		return self.__truediv__(other)
	
	def __le__(self, other):
		return self.__eq__(other)
	
	def __lt__(self, other):
		return False
	
	def __neg__(self):
		return NEGATIVE_INFINITY()
	
	def __pos__(self):
		return self
	
	def __radd__(self, other):
		return self.__add__(other)
	
	def __rfloordiv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return -1
		
		if isinstance(other, INFINITY):
			return 1
		
		return 0
	
	def __rmod__(self, other):
		if isinstance(other, (INFINITY, NEGATIVE_INFINITY)):
			return 0
		
		return other
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __round__(self, n=None):
		return self
	
	def __rpow__(self, power, modulo=None):
		if isinstance(power, NEGATIVE_INFINITY):
			return NEGATIVE_INFINITY()
		
		if 0 <= abs(power) < 1:
			return 0
		
		if power == 1:
			return 1
		
		if power == -1:
			return -1
		
		return self
	
	def __rsub__(self, other):
		if isinstance(other, INFINITY):
			return 0
		
		return NEGATIVE_INFINITY()
	
	def __rtruediv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return -1
		
		if isinstance(other, INFINITY):
			return 1
		
		return 0


class NEGATIVE_INFINITY:
	"""
	Represents negative infinity in a simplified numerical system.

	This class is designed to mimic the behavior of negative infinity in basic numerical operations,
	within a simplified framework that aims for practical utility rather than strict mathematical rigor.
	It treats negative infinity as an unbounded value less than any finite number, but simplifies
	operations with indeterminate forms to provide concrete, though not always mathematically
	definitive, results.

	**Key Simplifications and Concepts:**

	- **Simplified Infinity:**  `NEGATIVE_INFINITY` is not intended to be a mathematically rigorous
	  representation of infinity. Instead, it behaves like an extremely large negative number
	  for practical purposes within this simplified system.

	- **Indeterminate Forms:** Operations that result in mathematically indeterminate forms
	  (like `-∞ + ∞`, `-∞ - (-∞)`, `-∞ * 0`, `-∞ / -∞`, etc.) are simplified to return
	  specific concrete values (often 0, 1, or -1) for ease of use in programmatic contexts,
	  rather than raising errors or returning NaN-like values.  These simplifications are design choices
	  to provide a usable, albeit not strictly mathematically accurate, infinity representation.

	- **Basic Arithmetic:** Standard arithmetic operations are overloaded to behave consistently with the intuitive understanding of negative infinity, such as:

		- `-∞ + x = -∞` for any finite number `x`
		- `-∞ * x = -∞` for `x > 0`
		- `-∞ * x = +∞` for `x < 0`
		- `-∞ / x = -∞` for `x > 0`
		- `-∞ / x = +∞` for `x < 0`
		- `x / -∞ = 0` for any finite number `x`
		- `(-∞) ** x = -∞` for most positive powers `x`
		- `x ** (-∞) = 0` for `x > 1`
		- `(-∞) ** 0 = 1` (simplified interpretation for this system)

	- **Comparisons:** Comparisons are designed to reflect negative infinity as the smallest value:

		- `-∞ < x` is always true for any value `x` not equal to `-∞`
		- `-∞ > x` is always false for any value `x`
		- `-∞ <= x` is always true
		- `-∞ >= x` is true only if `x` is also `-∞`

	- **Boolean Value:** `bool(NEGATIVE_INFINITY)` is defined as `False`.

	**Use Case:**

	This class is useful in scenarios where you need to represent and operate with the concept of
	negative infinity in a program, but strict mathematical accuracy for all edge cases and
	indeterminate forms is not critical.  It provides a pragmatic approach for handling
	infinite bounds or values in algorithms and calculations where a simplified infinite value is sufficient.

	**Important Note:** For applications requiring rigorous mathematical correctness with infinities,
	especially in symbolic computations or advanced numerical analysis, a more sophisticated
	representation and handling of indeterminate forms would be necessary. This class is a
	practical simplification, not a complete mathematical model.
	"""
	
	def __str__(self):
		return "NEGATIVE_INFINITY"
	
	def __repr__(self):
		return "NEGATIVE_INFINITY"
	
	def __abs__(self):
		return INFINITY()
	
	def __bool__(self):
		return False
	
	def __eq__(self, other):
		return isinstance(other, NEGATIVE_INFINITY)
	
	def __ge__(self, other):
		return self.__eq__(other)
	
	def __gt__(self, other):
		return False
	
	def __add__(self, other):
		if isinstance(other, INFINITY):
			return 0
		
		return self
	
	def __iadd__(self, other):
		return self.__add__(other)
	
	def __floordiv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 1
		
		if isinstance(other, INFINITY):
			return -1
		
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			raise ZeroDivisionError
		
		return self
	
	def __ifloordiv__(self, other):
		return self.__floordiv__(other)
	
	def __mod__(self, other):
		if isinstance(other, (INFINITY, NEGATIVE_INFINITY)):
			return 0
		
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			raise ZeroDivisionError
		
		return self
	
	def __imod__(self, other):
		return self.__mod__(other)
	
	def __mul__(self, other):
		if isinstance(other, (int, float, NEGATIVE_INFINITY)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			return 0
		
		return self
	
	def __imul__(self, other):
		return self.__mul__(other)
	
	def __pow__(self, power, modulo=None):
		if isinstance(power, NEGATIVE_INFINITY):
			return 0
		
		if power == 0:
			return 1
		
		return self
	
	def __ipow__(self, power, modulo=None):
		return self.__pow__(power, modulo)
	
	def __sub__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 0
		
		return self
	
	def __isub__(self, other):
		return self.__sub__(other)
	
	def __truediv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 1
		
		if isinstance(other, INFINITY):
			return -1
		
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			raise ZeroDivisionError
		
		return self
	
	def __itruediv__(self, other):
		return self.__truediv__(other)
	
	def __le__(self, other):
		return True
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __lt__(self, other):
		return self.__ne__(other)
	
	def __neg__(self):
		return INFINITY()
	
	def __pos__(self):
		return self
	
	def __radd__(self, other):
		return self.__add__(other)
	
	def __rfloordiv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 1
		
		if isinstance(other, INFINITY):
			return -1
		
		return 0
	
	def __rmod__(self, other):
		if isinstance(other, (INFINITY, NEGATIVE_INFINITY)):
			return 0
		
		return other
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __round__(self, n=None):
		return self
	
	def __rpow__(self, power, modulo=None):
		if 0 < abs(power) < 1:
			return INFINITY()
		
		if power == 1:
			return 1
		
		if power == -1:
			return -1
		
		return 0
	
	def __rsub__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 0
		
		return INFINITY()
	
	def __rtruediv__(self, other):
		if isinstance(other, NEGATIVE_INFINITY):
			return 1
		
		if isinstance(other, INFINITY):
			return -1
		
		return 0
