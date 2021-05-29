from setuptools import find_packages
from setuptools import setup


def dependencies(imported_file):
    """ __Doc__ Handles dependencies """
    with open(imported_file) as file:
        return file.read().splitlines()


setup(
    name="httpaste",
    description="A simple tool for pasting text remotely",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=dependencies("requirements.txt"),
    entry_points={
        'console_scripts': [
            "httpaste = httpaste.app:main"
        ]
    }
)
