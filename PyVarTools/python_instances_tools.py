import typing
import inspect


def get_function_parameters(
		function_: typing.Callable,
		excluding_parameters: typing.Optional[list[str]] = None
) -> dict[str, typing.Any]:
	"""
	Retrieves the parameters of a given function.

	Args:
		function_ (typing.Callable): The function to inspect.
		excluding_parameters (typing.Optional[list[str]]): A list of parameter names to exclude from the result. Defaults to None.

	Returns:
		dict[str, typing.Any]: A dictionary containing the function's parameters, excluding those specified in `excluding_parameters`.
		The keys are the parameter names, and the values are the corresponding `inspect.Parameter` objects.

	:Usage:
		def my_function(a, b, c=1):
			pass

		get_function_parameters(my_function)
		{'a': <Parameter "a">, 'b': <Parameter "b">, 'c': <Parameter "c=1">}

		get_function_parameters(my_function, excluding_parameters=['b', 'c'])
		{'a': <Parameter "a">}
	"""
	if excluding_parameters is None:
		excluding_parameters = []
	
	return {
		key: value
		for key, value in inspect.signature(function_).parameters.items()
		if key not in excluding_parameters
	}


def get_class_fields(
		class_: type,
		excluding_fields: typing.Optional[list[str]] = None,
		start_exclude: typing.Optional[list[str]] = None,
		end_exclude: typing.Optional[list[str]] = None
) -> dict[str, typing.Any]:
	"""
	Retrieves the fields (non-callable attributes) of a given class.

	Args:
		class_ (type): The class to inspect.
		excluding_fields (list[str], optional): A list of field names to exclude from the result. Defaults to None.
		start_exclude (list[str], optional): A list of strings that if field name starts with it, then exclude this field. Defaults to None.
		end_exclude (list[str], optional): A list of strings that if field name ends with it, then exclude this field. Defaults to None.

	Returns:
		dict[str, typing.Any]: A dictionary containing the class's fields, excluding those specified in `excluding_fields`,
		 and also excluding methods (callable attributes) and special attributes (dunder methods).

	:Usage:
		class MyClass:
			field1 = 1
			field2 = "hello"

			def my_method(self):
				pass

		get_class_fields(MyClass)
		{'field1': 1, 'field2': 'hello'}

		get_class_fields(MyClass, excluding_fields=['field1'])
		{'field2': 'hello'}
	"""
	if excluding_fields is None:
		excluding_fields = []
	
	if start_exclude is None:
		start_exclude = []
	
	if end_exclude is None:
		end_exclude = []
	
	start_exclude_func = lambda x: any(x.startswith(exclude) for exclude in start_exclude) if isinstance(start_exclude, list) else lambda x: False
	end_exclude_func = lambda x: any(x.endswith(exclude) for exclude in end_exclude) if isinstance(end_exclude, list) else lambda x: False
	
	return {
		key: value
		for key, value in class_.__dict__.items()
		if not start_exclude_func(key)
		and not end_exclude_func(key)
		and not callable(value)
		and key not in excluding_fields
	}
