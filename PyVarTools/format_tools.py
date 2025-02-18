from pandas import DataFrame
from typing import (
	Any,
	Callable,
	Hashable,
	Optional,
	Union
)


def format_integer(number: int, class_sep: str = " ") -> str:
	"""
	Formats an integer with a custom thousands' separator.

	Args:
		number (int): The integer to format.
		class_sep (str): The thousands separator to use. Defaults to " ".

	Returns:
		str: The formatted integer string.

	:Usage:
		format_integer(1234567)
		'1 234 567'

		format_integer(1234567, class_sep=",")
		'1,234,567'
	"""
	return "{:,d}".format(number).replace(",", class_sep)


def format_float(number: float, class_sep: str = " ", number_of_decimals: int = 2) -> str:
	"""
	Formats a float with a custom thousands separator and a specified number of decimal places.

	Args:
		number (float): The float to format.
		class_sep (str): The thousands separator to use. Defaults to " ".
		number_of_decimals (int): The number of decimal places to include. Defaults to 2.

	Returns:
		str: The formatted float string.

	:Usage:
		format_float(1234567.89)
		'1 234 567.89'

		format_float(1234567.89, class_sep=",", number_of_decimals=3)
		'1,234,567.890'
	"""
	return ("{:,.%df}" % number_of_decimals).format(number).replace(",", class_sep)


def format_data_frame(
		data_frame: DataFrame,
		float_format: Union[str, Callable[[float], str]] = "%.2f",
		integer_format: Union[str, Callable[[int], str]] = "%d",
		columns_split: Optional[str] = " || ",
		header_border: Optional[str] = "=",
		top_border: Optional[str] = "=",
		left_border: Optional[str] = "|| ",
		bottom_border: Optional[str] = "=",
		right_border: Optional[str] = " ||",
) -> str:
	"""
	Formats a Pandas DataFrame into a string representation with borders and custom formatting.

	Args:
		data_frame (DataFrame): The DataFrame to format.
		float_format (Union[str, Callable[[float], str]]): The format string or a callable function for float values. Defaults to "%.2f".
		integer_format (Union[str, Callable[[int], str]]): The format string or a callable function for integer values. Defaults to "%d".
		columns_split (Optional[str]): The string used to separate columns. Defaults to " || ".
		header_border (Optional[str]): The character used for the header border. Defaults to "=".
		top_border (Optional[str]): The character used for the top border. Defaults to "=".
		left_border (Optional[str]): The string used for the left border. Defaults to "|| ".
		bottom_border (Optional[str]): The character used for the bottom border. Defaults to "=".
		right_border (Optional[str]): The string used for the right border. Defaults to " ||".

	Returns:
		str: The formatted string representation of the DataFrame.

	:Usage:
		df = DataFrame({'A': [1, 2.5, 3], 'B': [4, 5, 6]})
		=============
		|| A  || B ||
		=============
		|| 1  || 4 ||
		|| 2.5|| 5 ||
		|| 3  || 6 ||
		=============
	"""
	new_dataframe: dict[Hashable, Any] = {}
	
	for header, column in data_frame.items():
		new_dataframe[header] = []
	
		for i in range(len(column)):
			value = data_frame[header].iloc[i]
	
			if str(type(value)).startswith("<class 'numpy"):
				value = value.item()
	
			if isinstance(value, int):
				if isinstance(integer_format, str):
					value = integer_format % value
				else:
					value = integer_format(value)
			elif isinstance(value, float):
				if isinstance(float_format, str):
					value = float_format % value
				else:
					value = float_format(value)
	
			new_dataframe[header].append(value)
	
	data_frame = DataFrame(
			{
				header.__str__(): [header.__str__()] +
				new_dataframe[header]
				for header, column in data_frame.items()
			}
	)
	
	columns_split = columns_split if columns_split is not None else ""
	right_border = right_border if right_border is not None else ""
	left_border = left_border if left_border is not None else ""
	
	size_of_columns = [len(max(column.tolist(), key=len)) for index, column in data_frame.items()]
	size_of_table = (
			sum(size_of_columns) +
			len(columns_split) *
			(len(size_of_columns) - 1) +
			len(left_border) +
			len(right_border)
	)
	
	for header, size_of_column in zip(data_frame.columns, size_of_columns):
		data_frame[header] = data_frame[header].apply(lambda value_: value_ + " " * (size_of_column - len(value_)))
	
	output_lines = [
		"%s%s%s" % (
				left_border,
				columns_split.join([column for column in row.values.tolist()]),
				right_border
		)
		for index, row in data_frame.iterrows()
	]
	
	if top_border is not None:
		output_lines.insert(0, top_border * size_of_table)
	
	if header_border is not None:
		output_lines.insert(2, header_border * size_of_table)
	
	if bottom_border is not None:
		output_lines.append(bottom_border * size_of_table)
	
	return "\n".join(output_lines)
