#!/usr/bin/python3

from setuptools import setup, find_packages


__author__ = 'taz'

setup(
    name='evaluation',
    version='0.1',
    description='evaluation of software development skills',
    author='Taz Elkikhia',
    author_email='aelkikhia@gmail.comi',
    tests_require=[
        "pycodestyle",
        "pytest"
    ],
    install_requires=[
        'Flask==1.0.2',
        'Flask-Cors==3.0.7',
        'Flask-JWT==0.3.2',
        'Flask-RESTful==0.3.7',
        'Flask-SQLAlchemy==2.4.0'
    ],
    test_suite='pytest',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
