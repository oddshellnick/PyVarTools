from parameterized import parameterized
from inspect import Parameter, signature
from unittest import (
	TestCase,
	TestLoader,
	TestSuite,
	TextTestRunner
)
from PyVarTools.python_instances_tools import (
	create_contains_exclude_function,
	create_end_exclude_function,
	create_name_exclude_function,
	create_start_exclude_function,
	create_value_exclude_function,
	get_class_attributes,
	get_function_parameters
)


class TestGetFunctionParameters(TestCase):
	def test_get_function_parameters_combined_exclude(self):
		def sample_function(
				param1,
				exclude_name,
				exclude_start_param,
				param_end_exclude_,
				param_contains_substr,
				param_value_exclude=None,
				param6="default"
		):
			pass

		def exclude_if_default_string(param_value: Parameter):
			return isinstance(param_value.default, str)

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param_value_exclude": signature(sample_function).parameters["param_value_exclude"],
		}
		
		self.assertEqual(
				get_function_parameters(
						sample_function,
						name_exclude="exclude_name",
						start_exclude="exclude_start_",
						end_exclude="_exclude_",
						contains_exclude="substr",
						value_exclude=exclude_if_default_string
				),
				expected_params
		)
	
	def test_get_function_parameters_contains_exclude_list(self):
		def sample_function(param1, param_substr1, param_substr2, param4):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param4": signature(sample_function).parameters["param4"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, contains_exclude=["substr1", "substr2"]),
				expected_params
		)
	
	def test_get_function_parameters_contains_exclude_str(self):
		def sample_function(param1, param_contains_substr, param3):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param3": signature(sample_function).parameters["param3"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, contains_exclude="substr"),
				expected_params
		)
	
	def test_get_function_parameters_end_exclude_list(self):
		def sample_function(param1, param_end1_, param_end2_, param4):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param4": signature(sample_function).parameters["param4"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, end_exclude=["_end1_", "_end2_"]),
				expected_params
		)
	
	def test_get_function_parameters_end_exclude_str(self):
		def sample_function(param1, param_exclude_end_, param3):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param3": signature(sample_function).parameters["param3"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, end_exclude="_end_"),
				expected_params
		)
	
	def test_get_function_parameters_method(self):
		class SampleClass:
			def sample_method(self, x, y=10):
				pass

		expected_params = {
			"self": signature(SampleClass.sample_method).parameters["self"],
			"x": signature(SampleClass.sample_method).parameters["x"],
			"y": signature(SampleClass.sample_method).parameters["y"],
		}
		
		self.assertEqual(get_function_parameters(SampleClass.sample_method), expected_params)
	
	def test_get_function_parameters_name_exclude_list(self):
		def sample_function(param1, exclude_param1, exclude_param2, param4):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param4": signature(sample_function).parameters["param4"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, name_exclude=["exclude_param1", "exclude_param2"]),
				expected_params
		)
	
	def test_get_function_parameters_name_exclude_str(self):
		def sample_function(param1, exclude_param, param3):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param3": signature(sample_function).parameters["param3"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, name_exclude="exclude_param"),
				expected_params
		)
	
	def test_get_function_parameters_no_exclude(self):
		def sample_function(a, b, c):
			pass

		expected_params = {
			"a": signature(sample_function).parameters["a"],
			"b": signature(sample_function).parameters["b"],
			"c": signature(sample_function).parameters["c"],
		}
		
		self.assertEqual(get_function_parameters(sample_function), expected_params)
	
	def test_get_function_parameters_no_parameters(self):
		def sample_function():
			pass

		self.assertEqual(get_function_parameters(sample_function), {})
	
	def test_get_function_parameters_start_exclude_list(self):
		def sample_function(param1, exclude_start1_param, exclude_start2_param, param4):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param4": signature(sample_function).parameters["param4"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, start_exclude=["exclude_start1_", "exclude_start2_"]),
				expected_params
		)
	
	def test_get_function_parameters_start_exclude_str(self):
		def sample_function(param1, exclude_start_param, param3):
			pass

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param3": signature(sample_function).parameters["param3"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, start_exclude="exclude_start_"),
				expected_params
		)
	
	def test_get_function_parameters_value_exclude(self):
		def sample_function(param1, param2=None, param3="default"):
			pass

		def exclude_if_default_none(param_value: Parameter):
			return param_value.default is None

		expected_params = {
			"param1": signature(sample_function).parameters["param1"],
			"param3": signature(sample_function).parameters["param3"],
		}
		
		self.assertEqual(
				get_function_parameters(sample_function, value_exclude=exclude_if_default_none),
				expected_params
		)
	
	def test_get_function_parameters_with_default(self):
		def sample_function(a, b=1, c="test"):
			pass

		expected_params = {
			"a": signature(sample_function).parameters["a"],
			"b": signature(sample_function).parameters["b"],
			"c": signature(sample_function).parameters["c"],
		}
		
		self.assertEqual(get_function_parameters(sample_function), expected_params)


class TestGetClassAttributes(TestCase):
	def test_get_class_attributes_builtin_methods_exclude(self):
		class SampleClass:
			custom_attr = 2
			
			def __init__(self):
				self.attr = 1
			
			def __str__(self):
				return "SampleClass instance"

		expected_attrs = {"custom_attr": {"value": 2, "type": int}}
		
		self.assertEqual(get_class_attributes(SampleClass, start_exclude="__"), expected_attrs)
	
	def test_get_class_attributes_combined_exclude(self):
		def exclude_string_value(value):
			return isinstance(value, str)

		class SampleClass:
			attr1 = 1
			exclude_name_attr = 2
			start_exclude_attr = 3
			attr_end_exclude = 4
			contains_substr_attr = 5
			exclude_value_attr = "exclude"
			attr7 = 7

		expected_attrs = {
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr7": {"value": 7, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(
						SampleClass,
						name_exclude="exclude_name_attr",
						start_exclude="start_exclude_",
						end_exclude="_exclude",
						contains_exclude="substr",
						value_exclude=exclude_string_value
				),
				expected_attrs
		)
	
	def test_get_class_attributes_contains_exclude_list(self):
		class SampleClass:
			attr1 = 1
			attr_substr1 = 2
			attr_substr2 = 3
			attr4 = 4

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr4": {"value": 4, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, contains_exclude=["substr1", "substr2"]),
				expected_attrs
		)
	
	def test_get_class_attributes_contains_exclude_str(self):
		class SampleClass:
			attr1 = 1
			attr_contains_substr = 2
			attr3 = 3

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr3": {"value": 3, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, contains_exclude="substr"),
				expected_attrs
		)
	
	def test_get_class_attributes_end_exclude_list(self):
		class SampleClass:
			attr1 = 1
			attr_end1 = 2
			attr_end2 = 3
			attr4 = 4

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr4": {"value": 4, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, end_exclude=["_end1", "_end2"]),
				expected_attrs
		)
	
	def test_get_class_attributes_end_exclude_str(self):
		class SampleClass:
			attr1 = 1
			attr_exclude_end = 2
			attr3 = 3

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr3": {"value": 3, "type": int},
		}
		
		self.assertEqual(get_class_attributes(SampleClass, end_exclude="_end"), expected_attrs)
	
	def test_get_class_attributes_instance_no_exclude(self):
		class SampleClass:
			class_attr = "class_val"
			
			def __init__(self):
				self.instance_attr = 1

		instance = SampleClass()
		
		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"__init__": {
				"type": type(SampleClass.__dict__["__init__"]),
				"value": SampleClass.__dict__["__init__"]
			},
			"instance_attr": {"value": 1, "type": int},
			"class_attr": {"value": "class_val", "type": str},
		}
		
		self.assertEqual(get_class_attributes(instance), expected_attrs)
	
	def test_get_class_attributes_name_exclude_list(self):
		class SampleClass:
			attr1 = 1
			exclude_attr1 = 2
			exclude_attr2 = 3
			attr4 = 4

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr4": {"value": 4, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, name_exclude=["exclude_attr1", "exclude_attr2"]),
				expected_attrs
		)
	
	def test_get_class_attributes_name_exclude_str(self):
		class SampleClass:
			attr1 = 1
			exclude_attr = 2
			attr3 = 3

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr3": {"value": 3, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, name_exclude="exclude_attr"),
				expected_attrs
		)
	
	def test_get_class_attributes_no_attributes(self):
		class EmptyClass:
			pass

		expected_attrs = {
			"__module__": {
				"type": type(EmptyClass.__dict__["__module__"]),
				"value": EmptyClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(EmptyClass.__dict__["__dict__"]),
				"value": EmptyClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(EmptyClass.__dict__["__doc__"]),
				"value": EmptyClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(EmptyClass.__dict__["__weakref__"]),
				"value": EmptyClass.__dict__["__weakref__"]
			}
		}
		
		self.assertEqual(get_class_attributes(EmptyClass), expected_attrs)
	
	def test_get_class_attributes_no_exclude(self):
		class SampleClass:
			class_attr = "class_val"
			instance_attr = 1
			_private_attr = 2
			__magic_attr__ = 3
			attr_annotated: int = 4

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"__annotations__": {
				"type": type(SampleClass.__dict__["__annotations__"]),
				"value": SampleClass.__dict__["__annotations__"]
			},
			"class_attr": {"value": "class_val", "type": str},
			"instance_attr": {"value": 1, "type": int},
			"_private_attr": {"value": 2, "type": int},
			"__magic_attr__": {"value": 3, "type": int},
			"attr_annotated": {"value": 4, "type": int},
		}
		
		self.assertEqual(get_class_attributes(SampleClass), expected_attrs)
	
	def test_get_class_attributes_start_exclude_list(self):
		class SampleClass:
			attr1 = 1
			exclude1_attr = 2
			exclude2_attr = 3
			attr4 = 4

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr4": {"value": 4, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, start_exclude=["exclude1_", "exclude2_"]),
				expected_attrs
		)
	
	def test_get_class_attributes_start_exclude_str(self):
		class SampleClass:
			attr1 = 1
			exclude_start_attr = 2
			attr3 = 3

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr3": {"value": 3, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, start_exclude="exclude_"),
				expected_attrs
		)
	
	def test_get_class_attributes_value_exclude(self):
		def exclude_string_value(value):
			return isinstance(value, str)

		class SampleClass:
			attr1 = 1
			attr2 = "exclude"
			attr3 = 3

		expected_attrs = {
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"attr1": {"value": 1, "type": int},
			"attr3": {"value": 3, "type": int},
		}
		
		self.assertEqual(
				get_class_attributes(SampleClass, value_exclude=exclude_string_value),
				expected_attrs
		)
	
	def test_get_class_attributes_with_annotations(self):
		class SampleClass:
			annotated_attr: str = "test"
			annotated_no_value: int

		expected_attrs = {
			"__module__": {
				"type": type(SampleClass.__dict__["__module__"]),
				"value": SampleClass.__dict__["__module__"]
			},
			"__dict__": {
				"type": type(SampleClass.__dict__["__dict__"]),
				"value": SampleClass.__dict__["__dict__"]
			},
			"__doc__": {
				"type": type(SampleClass.__dict__["__doc__"]),
				"value": SampleClass.__dict__["__doc__"]
			},
			"__weakref__": {
				"type": type(SampleClass.__dict__["__weakref__"]),
				"value": SampleClass.__dict__["__weakref__"]
			},
			"__annotations__": {
				"type": type(SampleClass.__dict__["__annotations__"]),
				"value": SampleClass.__dict__["__annotations__"]
			},
			"annotated_attr": {"value": "test", "type": str},
			"annotated_no_value": {"type": int},
		}
		
		self.assertEqual(get_class_attributes(SampleClass), expected_attrs)


class TestCreateExcludeFunctions(TestCase):
	@parameterized.expand([(["substr1", "substr2"],), ("substr",), (None,),])
	def test_create_contains_exclude_function(self, contains_exclude_input):
		exclude_func = create_contains_exclude_function(contains_exclude_input)
		
		if isinstance(contains_exclude_input, list):
			self.assertTrue(exclude_func("name_substr1_name"))
			self.assertTrue(exclude_func("name_substr2_name"))
			self.assertFalse(exclude_func("name_no_substr_name"))
		elif isinstance(contains_exclude_input, str):
			self.assertTrue(exclude_func("name_substr_name"))
			self.assertTrue(exclude_func("name_no_substr_name"))
		else:
			self.assertFalse(exclude_func("any_name"))
	
	@parameterized.expand([(["_end1", "_end2"],), ("_end",), (None,),])
	def test_create_end_exclude_function(self, end_exclude_input):
		exclude_func = create_end_exclude_function(end_exclude_input)
		
		if isinstance(end_exclude_input, list):
			self.assertTrue(exclude_func("name_end1"))
			self.assertTrue(exclude_func("name_end2"))
			self.assertFalse(exclude_func("name_end"))
		elif isinstance(end_exclude_input, str):
			self.assertTrue(exclude_func("name_end"))
			self.assertFalse(exclude_func("name_end_"))
		else:
			self.assertFalse(exclude_func("any_name"))
	
	@parameterized.expand([(["name1", "name2"],), ("name",), (None,),])
	def test_create_name_exclude_function(self, name_exclude_input):
		exclude_func = create_name_exclude_function(name_exclude_input)
		
		if isinstance(name_exclude_input, list):
			self.assertTrue(exclude_func("name1"))
			self.assertTrue(exclude_func("name2"))
			self.assertFalse(exclude_func("other_name"))
		elif isinstance(name_exclude_input, str):
			self.assertTrue(exclude_func("name"))
			self.assertFalse(exclude_func("other_name"))
		else:
			self.assertFalse(exclude_func("any_name"))
	
	@parameterized.expand([(["start1_", "start2_"],), ("start_",), (None,),])
	def test_create_start_exclude_function(self, start_exclude_input):
		exclude_func = create_start_exclude_function(start_exclude_input)
		
		if isinstance(start_exclude_input, list):
			self.assertTrue(exclude_func("start1_name"))
			self.assertTrue(exclude_func("start2_name"))
			self.assertFalse(exclude_func("no_start_name"))
		elif isinstance(start_exclude_input, str):
			self.assertTrue(exclude_func("start_name"))
			self.assertFalse(exclude_func("no_start_name"))
		else:
			self.assertFalse(exclude_func("any_name"))
	
	@parameterized.expand([(lambda x: x == "exclude",), (None,),])
	def test_create_value_exclude_function(self, value_exclude_input):
		exclude_func = create_value_exclude_function(value_exclude_input)
		
		if callable(value_exclude_input):
			self.assertEqual(exclude_func, value_exclude_input)
		else:
			self.assertTrue(callable(exclude_func))
			self.assertFalse(exclude_func(1))
			self.assertFalse(exclude_func("test"))


def python_instances_tools_test_suite():
	suite = TestSuite()
	test_loader = TestLoader()
	
	suite.addTest(test_loader.loadTestsFromTestCase(TestCreateExcludeFunctions))
	suite.addTest(test_loader.loadTestsFromTestCase(TestGetClassAttributes))
	suite.addTest(test_loader.loadTestsFromTestCase(TestGetFunctionParameters))
	
	return suite


if __name__ == "__main__":
	runner = TextTestRunner()
	runner.run(python_instances_tools_test_suite())
