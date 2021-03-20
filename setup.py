# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


requires = [
    'fabric==2.5.0',
    'click==7.1.1',
    'requests==2.23.0',
    'Jinja2==2.11.3',
]
tests_require = ['pytest', 'pytest-cache', 'pytest-cov']


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="wise-cli",
    version='0.0.1',
    description="Django deployments CLI",
    long_description="\n\n".join([open("README.rst").read()]),
    license='MIT',
    author="Victor Aguilar C.",
    author_email="victor@xiberty.com",
    url="https://wise-cli.readthedocs.org",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points={'console_scripts': [
        'wise = wise.cli:main']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'],
    extras_require={'test': tests_require},
    cmdclass={'test': PyTest})
