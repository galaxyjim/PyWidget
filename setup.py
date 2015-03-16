#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='PyWidget3',
      version='1.0',
      author="GalaxyJim",
      license="BSD",
      description='Gui tools for pyglet',
      url='https://www.github.com/galaxyjim/pywidget3',
      packages=find_packages(exclude=["tests","samples_and_tests"])
     )
