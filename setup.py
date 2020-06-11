#!/usr/bin/env python

from setuptools import setup

setup(
   name='nrao_interview',
   version="0.0.0",
   description='NRAO Interview exercise.',
   author='Camilo Valenzuela',
   author_email='camilo.valenzuela@alumnos.usm.cl',
   packages=['nrao_interview'],
   scripts=["scripts/nrao_script"],
   install_requires=['click', 'pandas', 'matplotlib', 'numpy'],
)
