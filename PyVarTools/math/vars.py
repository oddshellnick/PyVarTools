class INFINITY:
	"""
	Represents positive infinity in a numerical system.

	This class is designed to mimic the behavior of positive infinity in numerical operations.
	It represents an unbounded value that is greater than any finite number. It handles basic
	arithmetic operations and comparisons involving positive infinity.

	**Key Concepts:**

	- **Unbounded Positive Value:** `INFINITY` represents a value larger than any real number.

	- **Arithmetic Operations:** Defines how positive infinity behaves in basic arithmetic:

		- Addition: `∞ + x = ∞` for any finite number `x`, `∞ + (-∞) = SINGULARITY`, `∞ + ∞ = ∞`
		- Subtraction: `∞ - x = ∞` for any finite number `x`, `∞ - ∞ = SINGULARITY`, `x - ∞ = -∞`
		- Multiplication: `∞ * x = ∞` for `x > 0`, `∞ * x = -∞` for `x < 0`, `∞ * 0 = SINGULARITY`, `∞ * ±∞ = ±∞` accordingly.
		- Division: `∞ / x = ∞` for `x > 0`, `∞ / x = -∞` for `x < 0`, `x / ∞ = 0` for finite `x`, `∞ / ±∞ = SINGULARITY`.
		- Modulo: `∞ % x = SINGULARITY` for finite `x`, `x % ∞ = x` for finite `x`.
		- Power: `(∞) ** x = ∞` for `x > 0`, `(∞) ** x = 0` for `x < 0`, `(∞) ** 0 = SINGULARITY`, `x ** ∞ = ∞` for `abs(x) > 1`, `x ** ∞ = 0` for `0 <= abs(x) < 1`.

	- **Comparisons:**

		- `∞ > x` is true for any `x` not `INFINITY`.
		- `∞ < x` is false for any `x`.
		- `∞ >= x` is always true.
		- `∞ <= x` is true only if `x` is also `INFINITY`.

	- **Boolean Value:** `bool(INFINITY)` is defined as `True`.

	**Use Case:**

	Useful for representing upper bounds, handling limits, and in algorithms where positive infinity
	is a meaningful value. It allows for calculations involving positive infinity while attempting
	to maintain mathematical consistency where possible, and signaling undefined results with `SINGULARITY`.

	**Important Note:** This class provides a practical implementation of positive infinity, but behavior
	in indeterminate forms like `∞ - ∞` is simplified to return `SINGULARITY` to indicate an undefined result.
	For strict mathematical contexts, more rigorous handling might be required.
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
		if isinstance(other, (NEGATIVE_INFINITY, SINGULARITY)):
			return SINGULARITY()
		
		return self
	
	def __iadd__(self, other):
		return self.__add__(other)
	
	def __floordiv__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			raise ZeroDivisionError
		
		return SINGULARITY()
	
	def __ifloordiv__(self, other):
		return self.__floordiv__(other)
	
	def __mod__(self, other):
		if isinstance(other, (int, float)) and other == 0:
			raise ZeroDivisionError
		
		return SINGULARITY()
	
	def __imod__(self, other):
		return self.__mod__(other)
	
	def __mul__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			return SINGULARITY()
		
		if isinstance(other, NEGATIVE_INFINITY):
			return NEGATIVE_INFINITY()
		
		if isinstance(other, INFINITY):
			return self
		
		return SINGULARITY()
	
	def __imul__(self, other):
		return self.__mul__(other)
	
	def __pow__(self, power, modulo=None):
		if isinstance(power, (int, float)):
			if power > 0:
				return self
		
			if power < 0:
				return 0
		
			return SINGULARITY()
		
		if isinstance(power, NEGATIVE_INFINITY):
			return 0
		
		if isinstance(power, INFINITY):
			return self
		
		return SINGULARITY()
	
	def __ipow__(self, power, modulo=None):
		return self.__pow__(power, modulo)
	
	def __sub__(self, other):
		if isinstance(other, (INFINITY, SINGULARITY)):
			return SINGULARITY()
		
		return self
	
	def __isub__(self, other):
		return self.__sub__(other)
	
	def __truediv__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			raise ZeroDivisionError
		
		return SINGULARITY()
	
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
		if isinstance(other, (int, float)):
			return 0
		
		return SINGULARITY()
	
	def __rmod__(self, other):
		if isinstance(other, (int, float)):
			return other
		
		return SINGULARITY()
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __round__(self, n=None):
		return self
	
	def __rpow__(self, power, modulo=None):
		if isinstance(power, (int, float)):
			if power < 0:
				return SINGULARITY()
		
			if power == 0:
				return 0
		
			if power < 1:
				return 0
		
			if power == 1:
				return 1
		
			if power > 1:
				return INFINITY()
		
		if isinstance(power, INFINITY):
			return self
		
		return SINGULARITY()
	
	def __rsub__(self, other):
		if isinstance(other, SINGULARITY):
			return SINGULARITY()
		
		return NEGATIVE_INFINITY()
	
	def __rtruediv__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return INFINITY()
		
			if other < 0:
				return NEGATIVE_INFINITY()
		
			return SINGULARITY()
		
		return SINGULARITY()


class NEGATIVE_INFINITY:
	"""
	Represents negative infinity in a numerical system.

	This class is designed to mimic the behavior of negative infinity in numerical operations.
	It represents an unbounded value that is less than any finite number. It handles basic
	arithmetic operations and comparisons involving negative infinity.

	**Key Concepts:**

	- **Unbounded Negative Value:** `NEGATIVE_INFINITY` represents a value smaller than any real number.

	- **Arithmetic Operations:** Defines how negative infinity behaves in basic arithmetic:

		- Addition: `-∞ + x = -∞` for any finite number `x`, `-∞ + ∞ = SINGULARITY`, `-∞ + -∞ = -∞`
		- Subtraction: `-∞ - x = -∞` for any finite number `x`, `-∞ - (-∞) = SINGULARITY`, `x - (-∞) = ∞`
		- Multiplication: `-∞ * x = -∞` for `x > 0`, `-∞ * x = ∞` for `x < 0`, `-∞ * 0 = SINGULARITY`, `-∞ * ±∞ = ±∞` accordingly.
		- Division: `-∞ / x = -∞` for `x > 0`, `-∞ / x = ∞` for `x < 0`, `x / -∞ = 0` for finite `x`, `-∞ / ±∞ = SINGULARITY`.
		- Modulo: `-∞ % x = SINGULARITY` for finite `x`, `x % -∞ = x` for finite `x`.
		- Power: `(-∞) ** x = -∞` for `x > 0`, `(-∞) ** x = 0` for `x < 0`, `(-∞) ** 0 = SINGULARITY`, `x ** -∞ = 0` for `abs(x) > 1`, `x ** -∞ = ∞` for `0 < abs(x) < 1`.

	- **Comparisons:**

		- `-∞ < x` is true for any `x` not `NEGATIVE_INFINITY`.
		- `-∞ > x` is false for any `x`.
		- `-∞ <= x` is always true.
		- `-∞ >= x` is true only if `x` is also `NEGATIVE_INFINITY`.

	- **Boolean Value:** `bool(NEGATIVE_INFINITY)` is defined as `True`.

	**Use Case:**

	Useful for representing lower bounds, handling limits, and in algorithms where negative infinity
	is a meaningful value. It allows for calculations involving negative infinity while attempting
	to maintain mathematical consistency where possible, and signaling undefined results with `SINGULARITY`.

	**Important Note:** This class provides a practical implementation of negative infinity, but behavior
	in indeterminate forms like `-∞ + ∞` is simplified to return `SINGULARITY` to indicate an undefined result.
	For strict mathematical contexts, more rigorous handling might be required.
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
		if isinstance(other, (INFINITY, SINGULARITY)):
			return SINGULARITY()
		
		return self
	
	def __iadd__(self, other):
		return self.__add__(other)
	
	def __floordiv__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			raise ZeroDivisionError
		
		return SINGULARITY()
	
	def __ifloordiv__(self, other):
		return self.__floordiv__(other)
	
	def __mod__(self, other):
		if isinstance(other, (int, float)) and other == 0:
			raise ZeroDivisionError
		
		return SINGULARITY()
	
	def __imod__(self, other):
		return self.__mod__(other)
	
	def __mul__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			return SINGULARITY()
		
		if isinstance(other, NEGATIVE_INFINITY):
			return INFINITY()
		
		if isinstance(other, INFINITY):
			return self
		
		return SINGULARITY()
	
	def __imul__(self, other):
		return self.__mul__(other)
	
	def __pow__(self, power, modulo=None):
		if isinstance(power, (int, float)):
			if power > 0:
				return self
		
			if power < 0:
				return 0
		
			return SINGULARITY()
		
		return SINGULARITY()
	
	def __ipow__(self, power, modulo=None):
		return self.__pow__(power, modulo)
	
	def __sub__(self, other):
		if isinstance(other, (NEGATIVE_INFINITY, SINGULARITY)):
			return SINGULARITY()
		
		return self
	
	def __isub__(self, other):
		return self.__sub__(other)
	
	def __truediv__(self, other):
		if isinstance(other, (int, float)):
			if other > 0:
				return self
		
			if other < 0:
				return INFINITY()
		
			raise ZeroDivisionError
		
		return SINGULARITY()
	
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
		if isinstance(other, (int, float)):
			return 0
		
		return SINGULARITY()
	
	def __rmod__(self, other):
		if isinstance(other, (int, float)):
			return other
		
		return SINGULARITY()
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __round__(self, n=None):
		return self
	
	def __rpow__(self, power, modulo=None):
		if isinstance(power, (int, float)):
			if power == 0:
				return INFINITY()
		
			if abs(power) == 1:
				return SINGULARITY()
		
			if abs(power) < 1:
				return INFINITY()
		
			if abs(power) > 1:
				return 0
		
		if isinstance(power, INFINITY):
			return 0
		
		return SINGULARITY()
	
	def __rsub__(self, other):
		if isinstance(other, SINGULARITY):
			return SINGULARITY()
		
		return INFINITY()
	
	def __rtruediv__(self, other):
		if isinstance(other, (int, float)):
			return 0
		
		return SINGULARITY()


class SINGULARITY:
	"""
	Represents a singular or undefined numerical result.

	This class is used to denote results of mathematical operations that are undefined,
	indeterminate, or singular in nature. It serves as a placeholder for situations where
	a numerical operation cannot yield a meaningful or valid numerical outcome.

	**Key Concepts:**

	- **Undefined Result:** `SINGULARITY` is returned when an operation results in a value that is
	  not mathematically defined or is considered indeterminate (e.g., division by zero involving
	  infinity in some contexts, or certain operations with infinities themselves).

	- **Propagation of Singularity:** Any arithmetic operation involving `SINGULARITY` will typically
	  result in `SINGULARITY`. This reflects the idea that if one input to an operation is undefined,
	  the output is also generally undefined.

	- **Non-Comparable:** `SINGULARITY` is not comparable to other values, including itself, in terms of
	  less than, greater than, or less than or equal to, or greater than or equal to. Comparisons
	  like `<`, `>`, `<=`, `>=` will always return `False`.

	- **Equality:** `SINGULARITY` is only considered equal to another `SINGULARITY` instance.

	- **Boolean Value:** `bool(SINGULARITY)` is defined as `False`, indicating that a singular result
	  can be treated as a "not valid" or "failed" condition in a boolean context.

	**Use Case:**

	`SINGULARITY` is useful in numerical computations and symbolic mathematics where you need to
	explicitly represent and handle undefined or singular results without raising exceptions
	in every instance. It allows for operations to continue while carrying forward the information
	that a part of the calculation has become undefined.

	**Important Note:**  The behavior of `SINGULARITY` is designed to signal an undefined result.
	It is crucial to handle `SINGULARITY` appropriately in subsequent computations to avoid
	propagating undefined states unintentionally or leading to incorrect conclusions.
	"""
	
	def __str__(self):
		return "SINGULARITY"
	
	def __repr__(self):
		return "SINGULARITY"
	
	def __abs__(self):
		return self
	
	def __add__(self, other):
		return self
	
	def __bool__(self):
		return False
	
	def __floordiv__(self, other):
		return self
	
	def __ge__(self, other):
		return False
	
	def __gt__(self, other):
		return False
	
	def __le__(self, other):
		return False
	
	def __lt__(self, other):
		return False
	
	def __mod__(self, other):
		return self
	
	def __mul__(self, other):
		return self
	
	def __eq__(self, other):
		return isinstance(other, SINGULARITY)
	
	def __ne__(self, other):
		return not self.__eq__(other)
	
	def __neg__(self):
		return self
	
	def __pos__(self):
		return self
	
	def __pow__(self, power, modulo=None):
		return self
	
	def __radd__(self, other):
		return self
	
	def __rfloordiv__(self, other):
		return self
	
	def __rmod__(self, other):
		return self
	
	def __rmul__(self, other):
		return self
	
	def __round__(self, n=None):
		return self
	
	def __rpow__(self, power, modulo=None):
		return self
	
	def __rsub__(self, other):
		return self
	
	def __rtruediv__(self, other):
		return self
	
	def __sub__(self, other):
		return self
	
	def __truediv__(self, other):
		return self
