#!/usr/bin/env python

from distutils.core import setup

from drsession import __version__

setup(name='DRSession',
  version=__version__,
  description="Derek's Redis Session Middleware",
  author='Derek Anderson',
  author_email='public@kered.org',
  url='https://github.com/keredson/drsession',
  py_modules=['drsession'],
  install_requires=['redis'],
)
