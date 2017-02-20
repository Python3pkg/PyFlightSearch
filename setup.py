#!/usr/bin/env python3

from setuptools import find_packages, setup


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open('test-requirements.txt') as requirements:
    test_required = requirements.read().splitlines()

with open("README.rst") as readme:
    long_description = readme.read()


if __name__ == "__main__":
    setup(
        name='PyFlightSearch',
        version='0.2.0',
        description='Generate a Webpage using results from coala',
        author="The coala developers",
        maintainer="Lasse Schuirmann",
        maintainer_email=('lasse.schuirmann@gmail.com'),
        url='https://github.com/aerupt/PyFlightSearch',
        platforms='any',
        packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
        install_requires=required,
        tests_require=test_required,
        license="MIT",
        long_description=long_description
    )