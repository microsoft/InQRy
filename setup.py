#!/usr/bin/env python

from setuptools import setup

setup(name='PyBar',
      version='0.0.1',
      license='MIT',
      description='Generate QRCodes for a Physical Inventory',
      author='Eric Hanko',
      author_email='v-erhank@microsoft.com',
      packages=['pybar'],
      long_description=open('README.md').read(),
      install_requires=["qrcode >= 5.3.0"],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
