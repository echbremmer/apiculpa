from setuptools import find_packages
from setuptools import setup

setup(
    name="BadApi",
    version="0.1.0",
    url="https://github.com/echbremmer/badapi",
    author="Emile Bremmer",
    description="A simple way to run a bad performing and unreliable dummy API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["Click"],
    entry_points={"console_scripts": ["badapi = badapi.cli:start_command"]},
)
