import pathlib
from setuptools import find_packages, setup

def get_file(file_name: str) -> str:
	file_path = pathlib.Path(file_name)

	if file_path.is_file():
		return open(file_path, "r", encoding="utf-8").read()
	else:
		raise FileNotFoundError(f"{file_name} not found")


def get_long_description() -> str:
	return get_file("long_description.md")


def get_install_requires() -> list[str]:
	return get_file("requirements.txt").splitlines()


def get_description() -> str:
	return get_file("description.txt")


setup(
		name="PyVarTools",
		version="1.4.1",
		author="oddshellnick",
		author_email="oddshellnick.programming@gmail.com",
		description=get_description(),
		long_description=get_long_description(),
		long_description_content_type="text/markdown",
		packages=find_packages(exclude=["unit_tests*"]),
		install_requires=get_install_requires(),
)
