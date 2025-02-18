import pathlib
from setuptools import find_packages, setup


def get_long_description() -> str:
	long_description_path = pathlib.Path("long_description.md")
	
	if long_description_path.is_file():
		return open(long_description_path, "r", encoding="utf-8").read()
	else:
		raise FileNotFoundError("long_description.md not found")


def get_install_requires() -> list[str]:
	requirement_path = pathlib.Path("requirements.txt")
	
	if requirement_path.is_file():
		return open(requirement_path, "r", encoding="utf-8").read().splitlines()
	else:
		raise FileNotFoundError("requirements.txt not found")


def get_description() -> str:
	description_path = pathlib.Path("description.txt")
	
	if description_path.is_file():
		return open(description_path, "r", encoding="utf-8").read()
	else:
		raise FileNotFoundError("description.txt not found")


setup(
		name="PyVarTools",
		version="1.4.0",
		author="oddshellnick",
		author_email="oddshellnick.programming@gmail.com",
		description=get_description(),
		long_description=get_long_description(),
		long_description_content_type="text/markdown",
		packages=find_packages(exclude=["unit_tests*"]),
		install_requires=get_install_requires(),
)
