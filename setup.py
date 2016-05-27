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
    packages=find_packages(exclude=['djfiles.tests']),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to upload files via admin panel.',
    long_description=README,
    url='https://github.com/luminousmen/djfiles',
    author='Bobrov Kirill',
    author_email='miaplanedo@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4' 
        'Programming Language :: Python :: 3.5'
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
