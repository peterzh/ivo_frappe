# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ivo/__init__.py
from ivo import __version__ as version

setup(
	name='ivo',
	version=version,
	description='Frappe platform for Ivo database',
	author='Peter Zatka-Haas',
	author_email='petetr@peterzh.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
