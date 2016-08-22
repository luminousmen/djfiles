# -*- coding: utf-8 -*-

import os
import io
from setuptools import setup, find_packages


with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()
try:
    import pypandoc
    long_description = pypandoc.convert(long_description, 'rst', 'md')
    long_description = long_description.replace('\r', '')
    with io.open('README.rst', mode='w', encoding='utf-8') as f:
        f.write(long_description)
except (ImportError, OSError):
    print("!!! Can't convert README.md - install pandoc and/or pypandoc.")


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-djfiles',
    version='0.2',
    packages=find_packages(exclude=['djfiles.tests']),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to upload files via admin panel.',
    long_description=long_description,
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'slugify',
    ],
)
