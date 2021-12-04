import os
import codecs
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fd:
    long_description = "\n" + fd.read()

VERSION = '0.0.0'
DESCRIPTION = "A python logger module for the codeCTRL application"
LONG_DESCRIPTION = long_description
SEARCH_KEYWORDS=[
        'pwnCTRL',
        'codeCTRL',
        'logging',
        "source code analysis",
        "source code",
        "analysis",
        "security",
        "vulnerability research"
        ]

DEPENDENCIES=[
        'cbor2'
        ]

setup(
        name="codectrl",
        version=VERSION,
        author="pwnCTRL",
        author_email="cotact@pwnctrl.com",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=DEPENDENCIES,
        keywords=SEARCH_KEYWORDS,
        classifiers=[
            "Development Status :: First stable version, not complete",
            "Intended Audience :: Package is intended for vulnerability research and other code-review",
            "Programming Language :: python :: 3",
            "Operating system :: Unix",
            "Operating system :: MacOS :: MacOS X",
            "Operating system :: Microsoft :: Windows"
            ]
        )
