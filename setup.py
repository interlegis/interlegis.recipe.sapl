# -*- coding: utf-8 -*-
"""
This module contains the tool of il.recipe.sapl
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0a1'

long_description = (
    read('README.rst')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('il', 'recipe', 'sapl', 'README.rst')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.rst')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.rst')
    + '\n' +
    'Download\n'
    '********\n')

entry_point = 'il.recipe.sapl:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'zc.buildout']

setup(name='il.recipe.sapl',
    version=version,
    description="",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
    keywords='sapl interelgis buildout recipe',
    author='Gustavo Lepri',
    author_email='gustavolepri@gmail.com',
    url='https://github.com/interlegis/il.recipe.sapl',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['il', 'il.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zc.buildout',
        'zope.globalrequest==1.0'
    ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite='il.recipe.sapl.tests.test_docs.test_suite',
    entry_points=entry_points,
)
