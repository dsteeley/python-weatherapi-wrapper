import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_requirements(requirements_file):
    with open(requirements_file) as f:
        required_packages = f.read().splitlines()
    return required_packages


setup(
    name="weatherapi",
    python_requires=">=3.8,<4.0",
    version="0.0.1",
    author="Jozef Tkocz",
    author_email="jozeftkocz@gmail.com",
    description=(
        "Python wrapper for the weather API provided by https://www.weatherapi.com/"
    ),
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
    long_description=read("README.md"),
)
