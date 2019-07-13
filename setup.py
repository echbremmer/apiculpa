from setuptools import find_packages
from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="Apiculpa",
    version="0.1.0",
    url="https://github.com/echbremmer/apiculpa",
    author="Emile Bremmer",
    description="A simple way to configure and run a poor performing and unreliable dummy API",
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Development Tools',
        'License :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
],
    keywords='dummy api test server',
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["Click"],
    entry_points={"console_scripts": ["apiculpa = apiculpa.cli:run_command"]},
    project_urls={
        'Bug Reports': 'https://github.com/echbremmer/apiculpa/issues',
        'Source': 'https://github.com/echbremmer/apiculpa',
},

)
