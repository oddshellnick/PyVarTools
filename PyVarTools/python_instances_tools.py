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


def get_class_attributes(
		class_: type,
		name_exclude: typing.Optional[typing.Union[list[str], str]] = None,
		start_exclude: typing.Optional[typing.Union[list[str], str]] = None,
		end_exclude: typing.Optional[typing.Union[list[str], str]] = None
) -> dict[str, typing.Any]:
	"""
	Retrieves the attributes of a given class, allowing for exclusion based on name patterns.

	Args:
		class_ (type): The class to inspect.
		name_exclude (typing.Optional[typing.Union[list[str], str]]): A list or a single string of attribute names to exclude from the result. Defaults to None.
		start_exclude (typing.Optional[typing.Union[list[str], str]]): A list or a single string. If an attribute name starts with any of these strings, it will be excluded. Defaults to None.
		end_exclude (typing.Optional[typing.Union[list[str], str]]): A list or a single string. If an attribute name ends with any of these strings, it will be excluded. Defaults to None.

	Returns:
		dict[str, typing.Any]: A dictionary containing the class's instances (attributes), excluding those matching the exclusion criteria.

	:Usage:
		class MyClass:
			instance1 = 1
			instance2 = "hello"
			_private_instance = "secret"
			instance_with_suffix_ = True

		get_class_instances(MyClass)
		{'instance1': 1, 'instance2': 'hello', '_private_instance': 'secret', 'instance_with_suffix_': True}

		get_class_instances(MyClass, name_exclude='_private_instance')
		{'instance1': 1, 'instance2': 'hello', 'instance_with_suffix_': True}

		get_class_instances(MyClass, start_exclude='_')
		{'instance1': 1, 'instance2': 'hello', 'instance_with_suffix_': True}

		get_class_instances(MyClass, end_exclude='_')
		{'instance1': 1, 'instance2': 'hello', '_private_instance': 'secret'}

		get_class_instances(MyClass, name_exclude=['_private_instance', 'instance_with_suffix_'], start_exclude='instance', end_exclude='2')
		{}
	"""
	name_exclude_func: typing.Callable[[str], bool] = (
			(lambda x: x in name_exclude)
			if isinstance(name_exclude, list)
			else (lambda x: x == name_exclude)
			if isinstance(name_exclude, str)
			else (lambda x: False)
	)
	start_exclude_func: typing.Callable[[str], bool] = (
			(lambda x: any(x.startswith(exclude) for exclude in start_exclude))
			if isinstance(start_exclude, list)
			else (lambda x: x.startswith(start_exclude))
			if isinstance(start_exclude, str)
			else (lambda x: False)
	)
	end_exclude_func: typing.Callable[[str], bool] = (
			(lambda x: any(x.endswith(exclude) for exclude in end_exclude))
			if isinstance(end_exclude, list)
			else (lambda x: x.endswith(end_exclude))
			if isinstance(end_exclude, str)
			else (lambda x: False)
	)
	
	return {
		key: value
		for key, value in class_.__dict__.items()
		if not start_exclude_func(key)
		and not end_exclude_func(key)
		and not name_exclude_func(key)
	}
