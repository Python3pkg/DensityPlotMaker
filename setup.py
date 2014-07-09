#!/usr/bin/env python

from distutils.core import setup

setup(name='densplot',
      version='1.0',
      packages=['densplot'],
      scripts = ['bin/densplot'],
      license='LICENSE.txt',
      description='DensPlot package',
      long_description=open('README.txt').read(),
     )
