# setup.py
from setuptools import setup, find_packages

setup(
    name="nanoXchange",
    version="0.1.0",
    package_dir={"": "src"},  # <--- this tells setuptools to look inside src/
    packages=find_packages(where="src"),  # <--- this finds packages inside src/
)
