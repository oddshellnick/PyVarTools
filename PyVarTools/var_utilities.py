import re
import typing
import datetime


def date_range(
		start_date: datetime.datetime,
		end_date: datetime.datetime,
		step: datetime.timedelta
) -> typing.Generator[datetime.datetime, typing.Any, None]:
	"""
	Generates a sequence of dates within a given range.

	Args:
		start_date (datetime.datetime): The starting date of the range.
		end_date (datetime.datetime): The ending date of the range (exclusive).
		step (timedelta): The time increment between each generated date.

	Returns:
		typing.Generator[datetime.datetime, typing.Any, None]: A generator yielding datetime objects.

	:Usage:
		start = datetime(2024, 1, 1)
		end = datetime(2024, 1, 5)
		delta = timedelta(days=1)
		for date in date_range(start, end, delta):
			print(date)

		2024-01-01 00:00:00
		2024-01-02 00:00:00
		2024-01-03 00:00:00
		2024-01-04 00:00:00
	"""
	while start_date < end_date:
		yield start_date
		start_date += step


def check_string_is_IPv4(string: str) -> bool:
	"""
	Checks if a given string is a valid IPv4 address.

	Args:
		string (str): The string to check.

	Returns:
		bool: True if the string is a valid IPv4 address, False otherwise.

	:Usage:
		check_string_is_IPv4("192.168.1.1")
		True

		check_string_is_IPv4("192.168.1.1:8080")
		True

		check_string_is_IPv4("256.256.256.256")
		False

		check_string_is_IPv4("invalid ip")
		False
	"""
	string_search = re.search(r"\A(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(?::\d{1,5})?\Z", string)
	
	if string_search:
		return all(0 <= int(group) <= 255 for group in string_search.groups())
	else:
		return False
