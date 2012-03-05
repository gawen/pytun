#!/usr/bin/env python

try:
    from setuptools import setup

except:
    from distutils.core import setup

import os

import pytun

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pytun",
    description = "Python TUN/TAP tunnel module",
    
    py_modules = ["pytun"],
    test_suite = "tests",

    version = pytun.__version__,
    author = pytun.__author__,
    author_email = pytun.__email__,
    url = "https://github.com/Gawen/pytun",
    license = pytun.__license__,
    long_description = read("README.md"),


    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
