#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='gvSelect',
      version='1.0-dev',
      description='Read and write gadgetviewer selection files in python',
      author='Simon Gibbons',
      author_email='sljg2@ast.cam.ac.uk',
      url='https://github.com/simongibbons/gvSelect',
      packages=['gvSelect'],
      install_requires=['numpy', 'fortranfile']
     )
