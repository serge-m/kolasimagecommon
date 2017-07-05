#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='kolasimagecommon',
      version='0.0.1',
      description='Common interfaces for image processing',
      author='sergem',
      author_email='sbmatyunin@gmail.com',
      url='https://serge-m.github.io',
      install_requires=required,
      packages=['kolasimagecommon'],
     )


