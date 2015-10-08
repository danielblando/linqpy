# -*- coding: utf-8 -*-
__author__ = 'Daniel'

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='linqpy',
    version='0.0.1',
    url='https://github.com/danielblando/linqpy',
    license='MIT',
    description='Simple implementation of .NET Linq in python list.',
    author=u'Daniel Blando',
    author_email='daniel@blando.com.br',
    long_description=read('README'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
    ],
)
