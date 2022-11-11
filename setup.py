"""
Python library for the codectrl-logger program.

This library is used for setting up codectrl

More information on this can be found at:
https://github.com/Authentura/codectrl/
"""

import os
import codecs
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fd:
    long_description = "\n" + fd.read()

VERSION = "1.0.0"
DESCRIPTION = "A python logger module for the codeCTRL application"
LONG_DESCRIPTION = long_description
SEARCH_KEYWORDS=[
        "Authentura",
        "authentura",
        "pwnCTRL",
        "codeCTRL",
        "logging",
        "source code analysis",
        "source code",
        "analysis",
        "security",
        "vulnerability research"
        ]

DEPENDENCIES=[
        "cbor2==5.4.2"
        ]

setup(
        name="codectrl",
        version=VERSION,
        license="MIT",
        author="Authentura",
        author_email="contact@authentura.com",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=DEPENDENCIES,
        keywords=SEARCH_KEYWORDS,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.9",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows"
            ]
        )
