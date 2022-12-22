import os
import re
from setuptools import setup

_long_description = open('README.md').read()

setup(
    name = "librarymadi",
    version = "4.2.5",
    author = "mahdi nazmi",
    author_email = "nazmimahdi7@gmail.com",
    description = (" library robot Rubika"),
    license = "MIT",
    keywords = ["rubika","bot","robot","library","rubikalib","rubikalib.ml","rubikalib.ir","rubika.ir","librarymadi","librarymadi","Rubika","Python"],
    url = "https://github.com/nazmimahdi/madi_library.git",
    packages=['librarymadi'],
    long_description=_long_description,
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python :: Implementation :: PyPy",
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    ],
)