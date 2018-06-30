import os
from setuptools import setup
from io import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='dunderfile',
    version='0.0.1',
    description='Python emulation of __FILE__, __LINE__, etc.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikewadsten/dunderfile',
    author='Mike Wadsten',
    py_modules=["dunderfile"],
)
