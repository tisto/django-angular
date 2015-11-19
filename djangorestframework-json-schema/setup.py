# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_install_requires():
    requirements = []
    for line in open('requirements.txt').readlines():
        # skip comments and empty lines
        if line.startswith('#') or \
           line == '' or \
           line.startswith('http') or \
           line.startswith('git'):
            continue
        requirements.append(line)
    return requirements


setup(
    name='djangorestframework-json-schema',
    version=get_version('rest_framework_json_schema'),
    license='BSD',
    author='Timo Stollenwerk',
    author_email='tisto@plone.org',
    description='JSON Schema add-on for Django Rest Framework',
    url='https://github.com/tisto/djangorestframework-json-schema',
    keywords=['django', 'rest-framework', 'json', 'json schema'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=get_install_requires(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
