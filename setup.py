#!/usr/bin/env python


try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

setup(name='rnmfls',
      version='1.0',
      description='Rename files',
      author='Matt Giguere',
      author_email='matthew.giguere@yale.edu',
      url='https://github.com/mattgiguere/rnmfls',
      packages=['rnmfls'],
      install_requires=["numpy"],)

