#!/usr/bin/env python
from os.path import dirname, join
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

curr_dir = dirname(__file__)

import binilla

try:
    try:
        long_desc = open(join(curr_dir, "readme.rst")).read()
    except Exception:
        long_desc = open(join(curr_dir, "readme.md")).read()
except Exception:
    long_desc = 'Could not read long description from readme.'

setup(
    name='binilla',
    description='A universal binary structure editor built on supyr_struct.',
    long_description=long_desc,
    version='%s.%s.%s' % binilla.__version__,
    url='http://bitbucket.org/moses_of_egypt/binilla',
    author='Devin Bobadilla',
    author_email='MosesBobadilla@gmail.com',
    license='MIT',
    packages=[
        'binilla',
        'binilla.defs',
        'binilla.widgets',
        'binilla.widgets.field_widgets',
        'binilla.windows',
        ],
    package_data={
        '': ['*.txt', '*.md', '*.rst', '*.pyw'],
        'binilla': [
            'styles/*.*',
            ]
        },
    platforms=["POSIX", "Windows"],
    keywords="binilla, binary, data structure",
    # arbytmap can be removed from the dependencies if you cannot install
    # it for some reason, though it will prevent certain things from working.
    install_requires=[
        'supyr_struct>=1.4.0', 'arbytmap', 'threadsafe_tkinter', 'tkcolorpicker'],
    requires=[
        'supyr_struct>=1.4.0', 'arbytmap', 'threadsafe_tkinter', 'tkcolorpicker'],
    provides=['binilla'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        ],
    zip_safe=False,
    )
