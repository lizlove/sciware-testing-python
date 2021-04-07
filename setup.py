#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

with open('requirements_dev.txt', 'r') as f:
    dev_requirements = [l for l in f.read().split('\n') if l.strip()]
dev_requirements += requirements

setup(
    author="sciware",
    author_email='audreyr@example.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    extras_require={'dev': dev_requirements},
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords='sciware_testing_python',
    name='sciware_testing_python',
    packages=find_packages(include=['sciware_testing_python']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/audreyr/sciware_testing_python',
    version='0.1.0',
    zip_safe=False,
)
