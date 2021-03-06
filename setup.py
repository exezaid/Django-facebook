#!/usr/bin/env python

import os
from distutils.core import setup
from django_facebook import __version__, __maintainer__, __email__


license_text = open('LICENSE.txt').read()
long_description = open('README.md').read()

CLASSIFIERS = [
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering :: Mathematics',
                'Topic :: Software Development :: Libraries :: Python Modules'
              ]

DESCRIPTION = """Facebook open graph API auth backend implementation using
the Django web framework and python."""


setup(
    name = 'django-facebook',
    version = __version__,
    url = 'http://github.com/tschellenbach/Django-facebook',
    author = __maintainer__,
    author_email = __email__,
    license = license_text,
    packages = ['django_facebook'],
    data_files=[('', ['LICENSE.txt',
                      'README.md'])],
    description = DESCRIPTION,
    long_description=long_description,
    classifiers = CLASSIFIERS,
    install_requires = ('python-cjson', 'django-registration', 'PIL'),
)



