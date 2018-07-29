# -*- coding: utf-8 -*-
import codecs
import os
import re
from setuptools import setup


with open('README.md') as f:
	long_description = f.read()



setup(name='lightpush',
		description='A Simple package for ServerChan',
		long_description=long_description,
		long_description_content_type='text/markdown',
		version='0.1.1',
		author='anhenghuang',
		author_email='contact@anhenghuang.com',
		url='http://github.com/anhenghuang/lightpush',
		license='MIT',
		packages=['lightpush'],
		install_requires = ['requests'],
		zip_safe=False,
		classifiers=(
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		),
)
