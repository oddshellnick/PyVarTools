from inspect import Parameter, signature
from typing import (
	Any,
	Callable,
	Optional,
	Union
)


def create_value_exclude_function(value_exclude: Optional[Callable[[Any], bool]]) -> Callable[[Any], bool]:
	"""
	Creates a function to exclude attributes based on a custom value exclusion logic.

	Args:
		value_exclude (Optional[Callable[[Any], bool]]): A function that takes an attribute's value and returns True if it should be excluded.

	Returns:
		Callable[[Any], bool]: Returns the provided `value_exclude` function if it's callable, otherwise returns a function that always returns False.
	"""
	if isinstance(value_exclude, Callable):
		return value_exclude
	else:
		return lambda x: False


def create_contains_exclude_function(contains_exclude: Optional[Union[list[str], str]]) -> Callable[[str], bool]:
	"""
	Creates a function to exclude attribute names if they contain a specific substring.

	Args:
		contains_exclude (Optional[Union[list[str], str]]): A list or a single string. Attributes containing these substrings will be excluded.

	Returns:
		Callable[[str], bool]: A function that returns True if the input name should be excluded, False otherwise.
	"""
	if isinstance(contains_exclude, list):
		return lambda x: any(exclude in x for exclude in contains_exclude)
	elif isinstance(contains_exclude, str):
		return lambda x: contains_exclude in x
	else:
		return lambda x: False


def create_end_exclude_function(end_exclude: Optional[Union[list[str], str]]) -> Callable[[str], bool]:
	"""
	Creates a function to exclude attribute names based on an ending string.

	Args:
		end_exclude (Optional[Union[list[str], str]]): A list or a single string. Attributes ending with these will be excluded.

	Returns:
		Callable[[str], bool]: A function that returns True if the input name should be excluded, False otherwise.
	"""
	if isinstance(end_exclude, list):
		return lambda x: any(x.endswith(exclude) for exclude in end_exclude)
	elif isinstance(end_exclude, str):
		return lambda x: x.endswith(end_exclude)
	else:
		return lambda x: False


def create_start_exclude_function(start_exclude: Optional[Union[list[str], str]]) -> Callable[[str], bool]:
	"""
	Creates a function to exclude attribute names based on a starting string.

	Args:
		start_exclude (Optional[Union[list[str], str]]): A list or a single string. Attributes starting with these will be excluded.

	Returns:
		Callable[[str], bool]: A function that returns True if the input name should be excluded, False otherwise.
	"""
	if isinstance(start_exclude, list):
		return lambda x: any(x.startswith(exclude) for exclude in start_exclude)
	elif isinstance(start_exclude, str):
		return lambda x: x.startswith(start_exclude)
	else:
		return lambda x: False


def create_name_exclude_function(name_exclude: Optional[Union[list[str], str]]) -> Callable[[str], bool]:
	"""
	Creates a function to exclude attribute names based on exact match.

	Args:
		name_exclude (Optional[Union[list[str], str]]): A list or a single string of attribute names to exclude.

	Returns:
		Callable[[str], bool]: A function that returns True if the input name should be excluded, False otherwise.
	"""
	if isinstance(name_exclude, list):
		return lambda x: x in name_exclude
	elif isinstance(name_exclude, str):
		return lambda x: x == name_exclude
	else:
		return lambda x: False


def get_function_parameters(
		function_: Callable,
		name_exclude: Optional[Union[list[str], str]] = None,
		start_exclude: Optional[Union[list[str], str]] = None,
		end_exclude: Optional[Union[list[str], str]] = None,
		contains_exclude: Optional[Union[list[str], str]] = None,
		value_exclude: Optional[Callable[[Any], bool]] = None
) -> dict[str, Parameter]:
	"""
	Retrieves the parameters of a given function with flexible exclusion capabilities.
	Allows excluding parameters based on their names, name prefixes, name suffixes, or if their names contain specific substrings.
	Also supports excluding parameters based on a custom function that evaluates the parameter value.

	Args:
		function_ (Callable): The function to inspect.
		name_exclude (Optional[Union[list[str], str]]): A list or a single string of parameter names to exclude. Exact match is required. Defaults to None.
		start_exclude (Optional[Union[list[str], str]]): A list or a single string. Parameters whose names start with any of these strings will be excluded. Defaults to None.
		end_exclude (Optional[Union[list[str], str]]): A list or a single string. Parameters whose names end with any of these strings will be excluded. Defaults to None.
		contains_exclude (Optional[Union[list[str], str]]): A list or a single string. Parameters whose names contain any of these strings will be excluded. Defaults to None.
		value_exclude (Optional[Callable[[Any], bool]]): A function that takes a parameter value (inspect.Parameter object) and returns `True` if the parameter should be excluded, `False` otherwise. Defaults to None.

	Returns:
		dict[str, Parameter]: A dictionary containing the function's parameters that satisfy the exclusion criteria.
		Keys are parameter names, and values are corresponding `inspect.Parameter` objects.

	:Usage:
		def sample_function(param1, param_exclude_start, param_exclude_end_, param_contains_substr, param5=None):
			pass

		get_function_parameters(sample_function)
		# Expected Output (Parameter objects are represented by their names for brevity):
		# {'param1': <Parameter "param1">, 'param_exclude_start': <Parameter "param_exclude_start">, 'param_exclude_end_': <Parameter "param_exclude_end_">, 'param_contains_substr': <Parameter "param_contains_substr">, 'param5': <Parameter "param5=None">}

		get_function_parameters(sample_function, name_exclude='param1')
		# {'param_exclude_start': <Parameter "param_exclude_start">, 'param_exclude_end_': <Parameter "param_exclude_end_">, 'param_contains_substr': <Parameter "param_contains_substr">, 'param5': <Parameter "param5=None">}

		get_function_parameters(sample_function, start_exclude='param_exclude')
		# {'param1': <Parameter "param1">, 'param5': <Parameter "param5=None">}

		get_function_parameters(sample_function, end_exclude='_end_')
		# {'param1': <Parameter "param1">, 'param_exclude_start': <Parameter "param_exclude_start">, 'param_contains_substr': <Parameter "param_contains_substr">, 'param5': <Parameter "param5=None">}

		get_function_parameters(sample_function, contains_exclude='substr')
		# {'param1': <Parameter "param1">, 'param_exclude_start': <Parameter "param_exclude_start">, 'param_exclude_end_': <Parameter "param_exclude_end_">, 'param5': <Parameter "param5=None">}

		get_function_parameters(
			sample_function,
			name_exclude=['param5'],
			start_exclude='param_exclude',
			end_exclude='_end_',
			contains_exclude='substr'
		)
		# {'param1': <Parameter "param1">}

		def exclude_if_optional(param_value):
			return param_value.default != inspect._empty

		get_function_parameters(sample_function, value_exclude=exclude_if_optional)
		# {'param1': <Parameter "param1">, 'param_exclude_start': <Parameter "param_exclude_start">, 'param_exclude_end_': <Parameter "param_exclude_end_">, 'param_contains_substr': <Parameter "param_contains_substr">}
	"""
	name_exclude_func = create_name_exclude_function(name_exclude)
	start_exclude_func = create_start_exclude_function(start_exclude)
	end_exclude_func = create_end_exclude_function(end_exclude)
	contains_exclude_func = create_contains_exclude_function(contains_exclude)
	value_exclude_func = create_value_exclude_function(value_exclude)
	
	return {
		key: value
		for key, value in signature(function_).parameters.items()
		if not start_exclude_func(key)
		and not end_exclude_func(key)
		and not contains_exclude_func(key)
		and not name_exclude_func(key)
		and not value_exclude_func(value)
	}


def get_class_attributes(
		class_,
		name_exclude: Optional[Union[list[str], str]] = None,
		start_exclude: Optional[Union[list[str], str]] = None,
		end_exclude: Optional[Union[list[str], str]] = None,
		contains_exclude: Optional[Union[list[str], str]] = None,
		value_exclude: Optional[Callable[[Any], bool]] = None
) -> dict[str, dict[str, Union[Any, type]]]:
	"""
	Retrieves the attributes of a given class or instance, allowing for flexible exclusion based on name patterns and value conditions.
	This function can be used to inspect both class-level attributes and instance-level attributes.
	It aggregates attributes from the instance's `__dict__` and the class's `__dict__`, and also includes type annotations from `__annotations__`.

	Args:
		class_: The class or instance to inspect.
		name_exclude (Optional[Union[list[str], str]]): A list or a single string of attribute names to exclude. Exact match is required. Defaults to None.
		start_exclude (Optional[Union[list[str], str]]): A list or a single string. Attributes whose names start with any of these strings will be excluded. Defaults to None.
		end_exclude (Optional[Union[list[str], str]]): A list or a single string. Attributes whose names end with any of these strings will be excluded. Defaults to None.
		contains_exclude (Optional[Union[list[str], str]]): A list or a single string. Attributes whose names contain any of these strings will be excluded. Defaults to None.
		value_exclude (Optional[Callable[[Any], bool]]): A function that takes an attribute's value as input and returns `True` if the attribute should be excluded, `False` otherwise. Defaults to None.

	Returns:
		dict[str, dict[str, Union[Any, type]]]: A dictionary containing the attributes of the class or instance, excluding those matching the exclusion criteria.
		Keys are attribute names, and values are the corresponding attribute values.

	:Usage:
		class MyClass:
			class_instance = "class_val"
			instance1 = 1
			instance2 = "hello"
			_private_instance = "secret"
			instance_with_suffix_ = True
			instance_with_substring = "substr"

			def __init__(self):
				self.dynamic_instance = "dynamic"

		# Get class attributes
		get_class_attributes(MyClass)
		# Expected Output:
		# {'class_instance': 'class_val', 'instance1': 1, 'instance2': 'hello', '_private_instance': 'secret', 'instance_with_suffix_': True, 'instance_with_substring': 'substr'}

		# Get instance attributes
		my_instance = MyClass()
		get_class_attributes(my_instance)
		# Expected Output:
		# {'dynamic_instance': 'dynamic'}

		get_class_attributes(MyClass, name_exclude='_private_instance')
		# {'class_instance': 'class_val', 'instance1': 1, 'instance2': 'hello', 'instance_with_suffix_': True, 'instance_with_substring': 'substr'}

		get_class_attributes(MyClass, start_exclude='_')
		# {'class_instance': 'class_val', 'instance1': 1, 'instance2': 'hello', 'instance_with_suffix_': True, 'instance_with_substring': 'substr'}

		get_class_attributes(MyClass, end_exclude='_')
		# {'class_instance': 'class_val', 'instance1': 1, 'instance2': 'hello', '_private_instance': 'secret', 'instance_with_substring': 'substr'}

		get_class_attributes(MyClass, contains_exclude='substr')
		# {'class_instance': 'class_val', 'instance1': 1, 'instance2': 'hello', '_private_instance': 'secret', 'instance_with_suffix_': True}


		get_class_attributes(
			MyClass,
			name_exclude=['_private_instance', 'instance_with_suffix_'],
			start_exclude='instance',
			end_exclude='_',
			contains_exclude='substr'
		)
		# {'class_instance': 'class_val'}

		def exclude_string_values(value):
			return isinstance(value, str)

		get_class_attributes(MyClass, value_exclude=exclude_string_values)
		# {'instance1': 1}
	"""
	name_exclude_func = create_name_exclude_function(name_exclude)
	start_exclude_func = create_start_exclude_function(start_exclude)
	end_exclude_func = create_end_exclude_function(end_exclude)
	contains_exclude_func = create_contains_exclude_function(contains_exclude)
	value_exclude_func = create_value_exclude_function(value_exclude)
	
	if isinstance(class_, type):
		class_dict = class_.__dict__
	else:
		class_dict = class_.__dict__
		class_dict.update(class_.__class__.__dict__)
	
	attributes = {
		key: {"value": value, "type": type(value)}
		for key, value in class_dict.items()
		if not start_exclude_func(key)
		and not end_exclude_func(key)
		and not contains_exclude_func(key)
		and not name_exclude_func(key)
		and not value_exclude_func(value)
	}
	
	for key, annotation in class_dict.get("__annotations__", {}).items():
		if (
				not start_exclude_func(key)
				and not end_exclude_func(key)
				and not contains_exclude_func(key)
				and not name_exclude_func(key)
				and not value_exclude_func(annotation)
		):
			if key in attributes:
				attributes[key]["type"] = annotation
			else:
				attributes[key] = {"type": annotation}
	
	return attributes
