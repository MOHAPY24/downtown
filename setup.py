# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="downtown",
    version="0.1.0",
    description="A Python framework for making websites from Markdown and CSS files.",
    license="BSD-3",
    author="MOHAPY24",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.12",
    ]
)
