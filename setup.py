#!/usr/bin/env python

from distutils.core import setup

setup(name='densplot',
      version='1.0',
      packages=['densplot'],
      description=['Plotting free energy landscapes'],
      scripts = ['bin/densplot'],
      license='LICENSE.txt',
      url='https://github.com/ClementiGroup/DensityPlotMaker',
      description='DensPlot package',
      long_description=open('README.md').read(),
     )
