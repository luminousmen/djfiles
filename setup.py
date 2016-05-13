# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-djfiles',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A simple Django app to upload files and shit.',
    long_description=README,
    author='Kirill Bobrov',
    author_email='miaplanedo@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
