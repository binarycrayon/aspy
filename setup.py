import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "aspy",
    version = "0.1",
    author = "Yudi Xue",
    author_email = "yudi.xue@usask.ca",
    description = ("A basic implementation of Aspect Oriented programming features"),
    license = "BSD",
    keywords = "aspect aop",
    url = "http://packages.python.org/aspy",
    packages=['aspy', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
